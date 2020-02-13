
'''
  Solution set: a,b,c; d,c,e; f,e,g; h,g,i; j,i,b for total z is a solution of the equation system:
  ( 1 1 1 0 0 0 0 0 0 0 )                               ( z )
  ( 0 0 1 1 1 0 0 0 0 0 )                               ( z )
  ( 0 0 0 0 1 1 1 0 0 0 ) (a b c d e f g h i j )^T  =   ( z )
  ( 0 0 0 0 0 0 1 1 1 0 )                               ( z )
  ( 0 1 0 0 0 0 0 0 1 1 )                               ( z )

  This system has solutions:
  a = -z + x_1 - x_2 + x_3  + 2 * x_4 + x_5
  b = z - x_4 - x_5
  c = z - x_1 + x_2 - x_3 - x_4
  d = x_1
  e = -x_2 + x_3 + x_4
  f = x_2
  g = z - x_3 - x_4
  h = x_3
  i = x_4
  j = x_5

  For positive integers x_1, ..., x_5.

  a < d,f,h,j
  => a <= 6, x_1, x_2, x_3, x_5 >= 2
  Since a solution must only have positive integer entries, this gives us the constraints
  x_1 - x_2 + x_3 + 2*x_4 + x_5 > z
  x_4 + x_5                     < z
  x_1 - x_2 + x_3 + x_4         < z
  x_3 + x_4                     < z
  => max(x_4 + x_5; x_1 - x_2 + x_3 + x_4; x_3 + x_4) < z < x_1 - x_2 + x_3 + 2*x_4 + x_5

  Also x_3 + x_4 > x_2.

  At last, one of d, f, h, j must be 10, otherwise the digit string would have a length of 17.
'''

solution_set = []

used_nums = []
for x_2 in range(2, 11):
  f = x_2
  used_nums.append(f)
  for x_3 in [x for x in range(2, 11) if x not in used_nums]:
    h = x_3
    used_nums.append(h)
    for x_4 in [x for x in range(1, 11) if x not in used_nums]:
      i = x_4
      e = -x_2 + x_3 + x_4
      if e < 1 or e > 10 or e in used_nums:
        continue
      used_nums.append(i)
      used_nums.append(e)
      for x_1 in [x for x in range(2, 11) if x not in used_nums]:
        d = x_1
        used_nums.append(d)
        if x_1 == 10 or x_2 == 10 or x_3 == 10:
          x_5_set = [x for x in range(2, 10) if x not in used_nums]
        else:
          x_5_set = [10]
        for x_5 in x_5_set:
          a_plus_z = x_1 - x_2 + x_3 + 2*x_4 + x_5
          z_minus_b = x_4 + x_5
          z_minus_c = x_1 - x_2 + x_3 + x_4
          z_minus_g = x_3 + x_4

          if z_minus_b == z_minus_c or z_minus_b == z_minus_g or z_minus_c == z_minus_g:
            continue

          j = x_5
          used_nums.append(j)

          z_min = max(z_minus_b, z_minus_c, z_minus_g) + 1
          z_max = a_plus_z - 1

          for z in range(z_min, z_max + 1):
            a = a_plus_z - z
            if a > 6:
              continue
            if a in used_nums:
              continue
            if a > x_1 or a > x_2 or a > x_3 or a > x_5:
              continue
            used_nums.append(a)

            b = z - z_minus_b
            if b > 10 or b in used_nums:
              used_nums.remove(a)
              continue
            used_nums.append(b)

            c = z - z_minus_c
            if c > 10 or c in used_nums:
              used_nums.remove(a)
              used_nums.remove(b)
              continue
            used_nums.append(c)

            g = z - z_minus_g
            if g > 10 or g in used_nums:
              used_nums.remove(a)
              used_nums.remove(b)
              used_nums.remove(c)
              continue
            used_nums.append(g)

            solution_string = ""
            for x in [a, b, c,  d, c, e,  f, e, g,  h, g, i,  j, i, b]:
              solution_string += str(x)
            solution_set.append(int(solution_string))
            used_nums.remove(a)
            used_nums.remove(b)
            used_nums.remove(c)
            used_nums.remove(g)
          used_nums.remove(j)
        used_nums.remove(d)
      used_nums.remove(i)
      used_nums.remove(e)
    used_nums.remove(h)
  used_nums.remove(f)

print(solution_set)
print(max(solution_set))
