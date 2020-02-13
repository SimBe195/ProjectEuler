import math

"""
    a / b < 3 / 7 <= (a+1) / b <=> a < 3b / 7 <= (a+1) <=> a = floor(3b/7) - 1
    So for given denominator b, the largest possible a such that a/b < 3/7 is a = ceil(3b/7) - 1.
    Now we just iterate over the denominators and keep track of which one produced the fraction closest to 3/7.
"""

max_frac = (0, 1)

for b in range(2, 1000001):
  a = (math.floor(3*b/7) - 1)
  if a*max_frac[1] > b * max_frac[0]:
    max_frac = (a, b)

print(max_frac)
