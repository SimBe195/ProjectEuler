import math

def sieve_of_eratosthenes(N):
  prime_checklist = [True] * (N + 1)
  prime_checklist[0] = False
  prime_checklist[1] = False
  for n in range(2, N + 1):
    if not prime_checklist[n]:
      continue
    for k in range(2 * n, N + 1, n):
      prime_checklist[k] = False

  return prime_checklist, [n for n in range(N + 1) if prime_checklist[n]]

prime_checklist, primes = sieve_of_eratosthenes(1000000)

n = 3
while True:
  if prime_checklist[n]:
    n += 2
    continue
  decomp_found = False
  for p in primes:
    if p >= n:
      break
    if math.sqrt((n - p) / 2).is_integer():
      decomp_found = True
      break

  if not decomp_found:
    print("Solution n = %i found." % n)
    break

  n += 2