import numpy as np


def sieve_of_eratosthenes(N, primes_so_far=[]):
  max_prime_so_far = 0
  if len(primes_so_far) > 0:
    max_prime_so_far = primes_so_far[-1]

  if N <= max_prime_so_far:
    return primes_so_far

  prime_checklist = [True] * (N + 1)

  if max_prime_so_far > 0:
    for n in range(primes_so_far[-1]):
      prime_checklist[n] = False
    for p in primes_so_far:
      prime_checklist[p] = True
  else:
    prime_checklist[0] = False
    prime_checklist[1] = False

  for n in range(N + 1):
    if not prime_checklist[n]:
      continue
    for k in range(max((max_prime_so_far // n  + 1), 2) * n, N + 1, n):
      prime_checklist[k] = False

  return prime_checklist, [n for n, is_prime in enumerate(prime_checklist) if is_prime]


prime_checklist, primes_lt_1000 = sieve_of_eratosthenes(1000)
primes = list(primes_lt_1000)
max_len_consec = 0
a_b_max_len_consec = (0, 0)
max_checked = 1000
for a in range(-999, 1000):
  for b in primes_lt_1000:
    n = 0
    while True:
      f_n = n*n + a*n + b
      if f_n < 0:
        break
      if f_n > max_checked:
        prime_checklist, primes = sieve_of_eratosthenes(f_n, primes)
        max_checked = f_n
      if not prime_checklist[f_n]:
        break
      n += 1

    if n > max_len_consec:
      print("n^2 + %i*n + %i gave %i consecutive primes." % (a, b, n))
      max_len_consec = n
      a_b_max_len_consec = (a, b)

print(max_len_consec)
print(a_b_max_len_consec)
print(np.prod(a_b_max_len_consec))

