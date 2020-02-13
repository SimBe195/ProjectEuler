import numpy as np

"""
 Similar to Problem 81. Iterate over columns; for each one iterate over the entries from top to bottom and from bottom
 to top to find the best scores.
"""

with open("p082_matrix.txt", "r") as file:
  rows = []
  for line in file:
    rows.append(np.array([int(x) for x in line.split(',')]))
  A = np.stack(rows)

num_rows, num_cols = A.shape
S = A[:, 0]
for col in range(1, num_cols):
  S[0] += A[0, col]
  for row in range(1, num_rows):
    S[row] = A[row, col] + min(S[row], S[row-1])

  for row in reversed(range(num_rows-1)):
    S[row] = min(S[row], A[row, col] + S[row+1])

print(np.min(S))
