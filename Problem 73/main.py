import math

"""
  We need to count fractions a/b such that 1/3 < a/b < 1/2 <=> b/3 < a < b/2 <=> floor(b/3) + 1 <= a <= ceil(b/2) - 1.
  From these a we only count those that are coprime to b.
"""

frac_count = 0

for b in range(1, 12001):
  for a in range(math.floor(b/3) + 1, math.ceil(b/2)):
    if math.gcd(a, b) == 1:
      frac_count += 1

print(frac_count)
