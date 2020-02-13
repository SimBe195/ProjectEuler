
import numpy as np

"""
  Take a dynamic programming approach. For any entry (i, j) in the matrix A, the minimal path sum ending in (i, j) is
  S(i, j) = A[i, j] + min(S(i-1, j), S(i, j-1)).
  For memory efficiency we only ever need to store one row of S.
"""


with open("p081_matrix.txt", "r") as file:
  rows = []
  for line in file:
    rows.append(np.array([int(x) for x in line.split(',')]))
  A = np.stack(rows)

num_rows, num_cols = A.shape
S = np.zeros(num_cols, dtype=np.int)
S[0] = A[0, 0]
for col in range(1, num_cols):
  S[col] = A[0, col] + S[col-1]

for row in range(1, num_rows):
  S[0] += A[row, 0]
  for col in range(1, num_cols):
    S[col] = A[row, col] + min(S[col-1], S[col])
  print(S)

print(S[-1])
