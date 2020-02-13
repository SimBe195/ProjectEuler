import math

"""
  Search with memoization.
"""

def factorial_digit_sum(n):
  return sum([math.factorial(int(digit)) for digit in str(n)])


chain_lengths = {}
for n in [1, 2, 145, 40585]:
  chain_lengths[n] = 1
for n in [871, 872, 45361, 45362]:
  chain_lengths[n] = 2
for n in [169, 363601, 1454]:
  chain_lengths[n] = 3


def chain_length(n):
  if n in chain_lengths:
    return chain_lengths[n]
  length = chain_length(factorial_digit_sum(n)) + 1
  chain_lengths[n] = length
  return length


counter = 0
for n in range(1000001):
  if chain_length(n) == 60:
    counter += 1

print("Total count: %i" % counter)
