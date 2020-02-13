import math
import time
tic = time.perf_counter()

"""
  For a m x n grid the number of rectangles it contains is n*(n+1)*m*(m+1) / 4 (for all widths w in {1,..,n}
  and all heights h in {1,..,m} the number of rectangles of size w x h fitting into the grid is (n-w+1)*(m-h+1)
  => Gaussian summation)
  
  Iterate over values of m, n.
  For a given n, the best value for m can be calculated in the following way:
  n(n+1)m(m+1) / 4 ~ 2,000,000
  <=> m² + m - 8,000,000/(n²+n) ~ 0
  <=> m ~= 1/2 * (sqrt(1 + 32,000,000/(n²+n)) +- 1)
  So examine the closest integers to these.
  
  Also, for an upper bound on the iteration:
  n(n+1)m(m+1) / 4 <= U
  => n(n+1) <= 2*U
  => n <= 1/2 * (sqrt(8*U + 1) - 1)
  We can start with U = 2,000,100 for example
"""

best_size = (0, 0)
closest_count = 0
closest_dist = 2000000
upper_bound = math.floor(1/2 * (math.sqrt(16000801) - 1))

for n in range(1, upper_bound):
  x = 0.5 * math.sqrt(32000000 / (n*n + n) + 1)
  for m in [math.floor(x-0.5), math.ceil(x-0.5), math.floor(x+0.5), math.ceil(x+0.5)]:
    count = int(n*(n+1)*m*(m+1) / 4)
    dist = abs(2000000 - count)
    if dist < closest_dist:
      closest_dist = dist
      closest_count = count
      best_size = (m, n)
  n += 1

print("Best grid size: ", best_size)
print("Area: ", best_size[0] * best_size[1])
print("Number of rectangles: ", closest_count)

print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))
