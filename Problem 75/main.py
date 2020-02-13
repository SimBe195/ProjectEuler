from collections import Counter
import math

"""
  A known formula that uniquely generates all pythagorean triples is a = k * (m² - n²), b = k * 2mn, c = k * (m² + n²)
  for positive integers m, n, k with m > n coprime and not both odd.
  The sidelength of such a triangle is therefore a + b + c = 2 * k * m * (m + n).
  => Iterate over k, m, n such that 2*k*m*(m+n) <= 1500000.
"""

length_counter = Counter()
max_length = 1500000
for k in range(1, max_length + 1):
  max_m = math.floor(math.sqrt(max_length / (2*k)))
  for m in range(1, max_m + 1):
    max_n = math.floor(max_length / (2 * k * m) - m)
    max_n = min(max_n, m - 1)
    if m % 2 == 0:
      n_range = range(1, max_n + 1)
    else:
      n_range = range(2, max_n + 1, 2)

    for n in n_range:
      if math.gcd(m, n) == 1:
        L = 2 * k * m * (m + n)
        length_counter.update([L])

length_statistics = Counter(length_counter.values())
print(length_statistics[1])
