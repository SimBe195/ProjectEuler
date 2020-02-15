import math
import time
tic = time.perf_counter()


def sieve_of_eratosthenes(N):
  primes = [True] * (N + 1)
  primes[0] = False
  primes[1] = False
  for n in range(2, N + 1):
    if not primes[n]:
      continue
    for k in range(2 * n, N + 1, n):
      primes[k] = False

  return [n for n in range(N + 1) if primes[n]]


max_num = 50000000

primes = sieve_of_eratosthenes(math.ceil(math.sqrt(max_num)))
solution_set = set()

a_primes = [p for p in primes if p**2 < max_num]
b_primes = [p for p in a_primes if p**3 < max_num]
c_primes = [p for p in b_primes if p**4 < max_num]

for a in a_primes:
  for b in b_primes:
    x = a*a + b*b*b
    if x >= max_num:
      break
    for c in c_primes:
      num = x + c*c*c*c
      if num > max_num:
        break
      solution_set.add(num)

print(len(solution_set))
print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))
