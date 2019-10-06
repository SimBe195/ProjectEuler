import math

'''
  If the previous expansion is a/b, the next expansion is 1 + 1 / (1 + a/b) = (a + 2b) / (a+b).
  It is easy to verify that a common divisor of (a+2b) and (a+b) would also have to be a divisor of a and b, so
  if a and b don't have common divisors, the next expansion also has none, so we can disregard that.
'''


def num_digits(n):
  return len(str(n))


a, b = 3, 2
counter = 0

for n in range(2, 1001):
  a, b = a + 2*b, a+b
  if num_digits(a) > num_digits(b):
    counter += 1

print(counter)
