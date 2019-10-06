
def are_permutations(n_1, n_2):
  n_1_digits = list(str(n_1))
  n_1_digits.sort()
  n_2_digits = list(str(n_2))
  n_2_digits.sort()
  return n_1_digits == n_2_digits


sol_found = False
x = 1
while not sol_found:
  sol_found = True
  for k in range(2, 7):
    if not are_permutations(x, k*x):
      sol_found = False
      break

  if sol_found:
    print("Solution found!")
    print([k*x for k in range(1, 7)])

  x += 1
