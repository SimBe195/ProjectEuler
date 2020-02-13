
import time
tic = time.perf_counter()

"""
  In a cuboid of size a x b x c, the three candidates for the shortest path have lengths
  sqrt(a² + (b+c)²), sqrt(b² + (a+c)²), sqrt(c² + (a+b)²).
  Ignoring rotations we can assume a <= b <= c, then the shortest path has length l = sqrt(c² + (a+b)²).
  For this to be an integer, this means that (c, (a+b), l) is a pythagorean triple.
  => Iterate over pythagorean triples (x, y, z) with x, y < z. For each of these, there are 
  max(floor((2y - x)/2), 0) + max(floor((2x - y)/2), 0) + 2 corresponding cuboids, namely the ones with sides
  (x-y + k, y - k, y) for k in {0,..,floor((2y-x)/2)} (to ensure a <= b <= c) and
  (y-x + k, x - k, x) for k in {0,..,floor((2x-y)/2)}
"""

print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))
