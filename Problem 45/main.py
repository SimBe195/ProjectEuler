import math

def is_pentagonal(n):
  check_num = (math.sqrt(24 * n + 1) + 1) / 6
  return check_num.is_integer(), check_num

'''
H_n = n * (2n - 1) = 2*n^2 - n = 2 * (n^2 - 2*(1/4)*n + (1/4)^2) - 1/8
<=> H_n + 1/8 = 2 * (n - 1/4)^2
<=> (8*H_n/16 + 1/16) = (n - 1/4)^2
<=> sqrt(8*H_n + 1) / 4 = n - 1/4
<=> (sqrt(8*H_n + 1) + 1) / 4 = n
'''


def is_hexagonal(n):
  check_num = (math.sqrt(8*n + 1) + 1) / 4
  return check_num.is_integer(), check_num


def triangle_number(n):
  return int(n * (n+1) / 2)

k = 286
while True:
  tri = triangle_number(k)
  is_pent, pent_index = is_pentagonal(tri)
  is_hex, hex_index = is_hexagonal(tri)
  if is_pent and is_hex:
    print("Solution %i = T_%i = P_%i = H_%i found." % (tri, k, pent_index, hex_index))
    break
  k += 1

