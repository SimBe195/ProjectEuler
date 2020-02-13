import numpy as np
import time
tic = time.perf_counter()

"""
  Use the dijkstra algorithm to find the shortest path
"""

with open("p083_matrix.txt", "r") as file:
  rows = []
  for line in file:
    rows.append(np.array([int(x) for x in line.split(',')]))
  A = np.stack(rows)

S = np.full(A.shape, np.iinfo(np.int).max, dtype=np.int)
S[0, 0] = A[0, 0]
remaining = [coords for coords, _ in np.ndenumerate(S)]
while len(remaining) > 0:

  # Find nearest neighbour
  nearest_neighbour = (0, 0)
  dist = np.inf
  for x, y in remaining:
    if S[x, y] < dist:
      nearest_neighbour = (x, y)
      dist = S[x, y]
  x, y = nearest_neighbour
  S[x, y] = dist
  remaining.remove(nearest_neighbour)

  # Update adjacent nodes
  for d_x, d_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    x_, y_ = x + d_x, y + d_y
    if (x_, y_) in remaining:
      S[x_, y_] = min(S[x_, y_], A[x_, y_] + S[x, y])

print(S)
print(S[-1, -1])

print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))
