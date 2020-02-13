import math
import sys
from collections import Counter

sys.setrecursionlimit(100000)


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


def is_permutation_of(num1, num2):
  return sorted(str(num1)) == sorted(str(num2))


def euler_phi(prime_fact):
  prod = 1
  for p, exp in prime_fact.items():
    if exp > 0:
      prod *= (p-1)*p**(exp-1)
  return prod


class PrimeFactIterator:
  # Iterates over prime-factorizations less or equal to max_n, optionally only using a given list of primes.

  def __init__(self, max_n, primes=None):
    self.max_n = max_n
    if primes is None:
      self.primes = sieve_of_eratosthenes(self.max_n)
    else:
      self.primes = primes
    self.current_fact = Counter()
    self.current_n = 1

    self.stop_next = False

  def __iter__(self):
    return self

  def __next__(self):
    if self.stop_next:
      raise StopIteration

    fact = self.current_fact.copy()
    n = self.current_n

    for p in self.primes:
      prod_with_p = self.current_n * p
      if prod_with_p <= self.max_n:
        self.current_fact.update([p])
        self.current_n = prod_with_p
        break
      else:
        self.current_n //= p**self.current_fact[p]
        self.current_fact[p] = 0
        if p == self.primes[-1]:
          self.stop_next = True

    return fact, n


min_ratio = float("inf")
min_n = -1

primes = sieve_of_eratosthenes(10**7)[4:]  # If number contains factor 2, 3, 5 or 7, then n / phi(n) > 87109 / 79180.
counter = 0
for fact, n in PrimeFactIterator(10**7, primes):
  counter += 1
  if counter % 10000 == 0:
    print(counter)
  if n == 1:
    continue
  phi_n = euler_phi(fact)
  ratio = n / phi_n
  if ratio > min_ratio:
    continue

  if is_permutation_of(n, phi_n):
    min_ratio = ratio
    while primes[0] / (primes[0] - 1) > min_ratio:
      primes = primes[1:]
    min_n = n
    print("New minimum n: n = %i, phi(n) = %i" % (n, phi_n))

print("Best n: %i" % min_n)
print("Best ratio: %i" % min_ratio)
