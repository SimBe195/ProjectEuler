import functools
import math

"""
  We can generate partition numbers using the formula p(n) = sum_{k > 0} (-1)^(k+1) * p(n - k*(3k-1)/2).
  => Recursive formula with memoization
"""

@functools.lru_cache(maxsize=None)
def num_partitions(n):
  if n == 0:
    return 1

  sub_sum = 0
  for k in range(math.ceil(-(math.sqrt(24*n+1)-1)/6), math.floor((math.sqrt(24*n+1)+1)/6 + 1)):
    if k == 0:
      continue
    if k % 2 == 0:
      sign = -1
    else:
      sign = 1
    sub_sum += sign * num_partitions(n - int(k*(3*k-1)/2))
  return sub_sum


print(num_partitions(100))
