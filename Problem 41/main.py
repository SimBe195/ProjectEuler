import itertools
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


prime_checklist, primes = sieve_of_eratosthenes(10000000)
prime_checklist = {i: prime_checklist[i] for i in range(len(prime_checklist))}


def is_prime(n):
  if n in prime_checklist:
    return prime_checklist[n]

  for i in range(2, math.floor(math.sqrt(n))):
    if n % i == 0:
      prime_checklist[n] = False
      return False

  prime_checklist[n] = True
  return True


max_prime = 0
for length in range(1, 10):
  digits = [str(i) for i in range(1, length+1)]
  for perm in itertools.permutations(digits):
    num_string = ""
    for digit in perm:
      num_string += digit

    num = int(num_string)
    if is_prime(num):
      if num > max_prime:
        max_prime = num
      print("prime %i is pandigital" % num)

print("Maximum pandigital prime is %i" % max_prime)
