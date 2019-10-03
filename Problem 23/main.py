import numpy as np


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


def p_exponent(n, p):
  exponent = 0
  while n % p == 0:
    exponent += 1
    n /= p
  return exponent


max_num = 28123
primes = sieve_of_eratosthenes(max_num)

sum_divisors = [-1] * (max_num + 1)
sum_divisors[0] = 0
sum_divisors[1] = 1
abundant_numbers = []

for n in range(max_num + 1):
  for p in primes:
    n_times_p = n*p
    if n_times_p > max_num:
      break
    if sum_divisors[n_times_p] >= 0:
      continue
    p_exp = p_exponent(n, p)
    sum_divisors[n_times_p] = sum_divisors[n] + sum_divisors[int(n / (p**p_exp))] * p**(p_exp + 1)

sum_proper_divisors = [sd - n for n, sd in enumerate(sum_divisors)]
abundant_numbers = [n for n in range(max_num + 1) if sum_proper_divisors[n] > n]

total = 0
for n in range(max_num + 1):
  sum_of_abundants = False
  for ab in abundant_numbers:
    diff = n - ab
    if diff <= 0:
      continue
    if sum_proper_divisors[diff] > diff:
      sum_of_abundants = True
      break
  if not sum_of_abundants:
    total += n

print(total)
