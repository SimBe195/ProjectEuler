import math


def pentagonal_number(n):
  return int(n * (3*n - 1) / 2)


'''
P_k = n * (3n - 1) / 2 
<=> 2 * P_k = 3n^2 - n = 3*(n^2 - 1/3 n + (1/6)^2 + (1/6)^2) 
<=> 2 * P_k = 3 * (n - 1/6)^2 + 1/12
<=> 24 * P_k + 1 = 36 * (n - 1/6)^2
<=> sqrt(24*P_k + 1) = 6 * n - 1
<=> (sqrt(24 * P_k + 1) + 1) / 6
'''


def is_pentagonal(n):
  check_num = (math.sqrt(24 * n + 1) + 1) / 6
  return check_num.is_integer(), check_num


n = 2
sol_found = False
while not sol_found:
  pen_n = pentagonal_number(n)

  for m in range(n-1, 0, -1):
    print("check n = %i, m = %i" % (n, m))
    pen_m = pentagonal_number(m)
    sum_is_pent, _ = is_pentagonal(pen_n + pen_m)
    if not sum_is_pent:
      continue
    pen_diff = pen_n - pen_m
    diff_is_pent, index = is_pentagonal(pen_diff)
    if diff_is_pent:
      print("Solution P_%i = %i = P_%i - P_%i = %i - %i found." % (index, pen_diff, n, m, pen_n, pen_m))
      sol_found = True
      break
  n += 1

