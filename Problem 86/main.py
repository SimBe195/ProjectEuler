import math
import time
tic = time.perf_counter()

"""
  In a cuboid of size a x b x c, the three candidates for the shortest path have lengths
  sqrt(a² + (b+c)²), sqrt(b² + (a+c)²), sqrt(c² + (a+b)²).
  Ignoring rotations we can assume a <= b <= c, then the shortest path has length l = sqrt(c² + (a+b)²).
  => The search complexity can be reduced to M² by iteration over (a+b) instead of a and b
"""

cuboid_count = 0
max_sidelength = 0
max_cuboid_count = 1000000

while cuboid_count <= max_cuboid_count:
  max_sidelength += 1
  for a_plus_b in range(2, 2*max_sidelength+1):
    if math.sqrt(max_sidelength*max_sidelength + a_plus_b*a_plus_b).is_integer():
      cuboid_count += math.floor(a_plus_b / 2) - max(a_plus_b - max_sidelength - 1, 0)

print("Max sidelength: %i, cuboid counter: %i" % (max_sidelength, cuboid_count))
print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))
