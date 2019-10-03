
'''
We have c = p - a - b so a² + b² = c² <=> a² + b² = (p - a - b)² = p² + a² + b² + 2ab - 2ap - 2bp <=> p² = 2(ap + bp - ab)
'''


def num_solutions(p):
  if p % 2 != 0:
    return 0

  p_squared = p*p
  count = 0
  for a in range(1, p):
    for b in range(a, p - a):
      if 2 * (a*p + b*p - a*b) == p_squared:
        count += 1

  return count


max_p = -1
max_num_solutions = 0
for p in range(1001):
  num_sol = num_solutions(p)
  if num_sol > max_num_solutions:
    max_num_solutions = num_sol
    max_p = p

print(max_p, max_num_solutions)
