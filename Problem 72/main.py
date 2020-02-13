from collections import Counter

"""
  For a given denominator b, the number of numerators coprime to b is given by the euler totient function phi(b).
"""


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


frac_count = -1  # denominator 1 adds an unwanted 1 to the counter
for fact, n in PrimeFactIterator(10**6):
  frac_count += euler_phi(fact)

print(frac_count)
