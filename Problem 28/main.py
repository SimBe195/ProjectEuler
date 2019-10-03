
'''
The sum of the diagonals in a 1x1 grid is 1.
In a 3x3 grid it's 1 + (3 + 9) + (5 + 7) = 1 + 2 * 12 = 25.
In a 5x5 grid it's 1 + 2 * 12 + (13 + 25) + (17 + 21) = 1 + 2 * 12 + 2 * 38

In general the minimal number min_n in the n'th spiral (counting from the middle) is min_n = min_n-1 + 6*(n-1) + 2*n.
The maximal number max_n in the n'th spiral is max_n = min_n + 6*n.
The sum of diagonals in a (2*n+1) x (2*n+1) grid is 1 + sum_{k=1..n} 2 * (min_k + max_k) = 1 + sum_{k=1..n} 4 * min_n + 12*n.
1001 = 2*500 + 1, so we evaluate this sum for n = 500
'''

min_k = 1
sum_diag = 1
for k in range(1, 501):
  min_k += 6 * (k-1) + 2 * k
  sum_diag += 4 * min_k + 12 * k

print(sum_diag)
