import math

'''
  Wikipedia tells us that these equations are called "Pell's equations" and solutions can be found using continued fractions.
  https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
  If (x,y) is a solution of the equation x^2 - D*y^2 = 1 then the fraction x/y appears in the sequence of convergents
  of the continued fraction of sqrt(D).
'''


def continued_fraction_root(n):  # returns the continued fraction of sqrt(n)
  root_n = math.sqrt(n)
  intermediate_steps = [(int(root_n), (1, int(root_n)))]
  while True:
    prev_b, prev_c = intermediate_steps[-1][1]
    assert (n - prev_c**2) % prev_b == 0     # prev_b / (sqrt(n) - prev_c) = prev_b * (sqrt(n) + prev_c) / (n - prev_c^2)
    b = int((n - prev_c**2) / prev_b)        # = (sqrt(n) + prev_c) / b
    a = int((root_n + prev_c) / b)           # = a + (sqrt(n) - c) / b
    c = a * b - prev_c
    next_step = (a, (b, c))
    if next_step in intermediate_steps:     # have already seen this step -> period found
      prev_index = intermediate_steps.index(next_step)
      result = [[], []]
      for i in range(prev_index):
        result[0].append(intermediate_steps[i][0])
      for i in range(prev_index, len(intermediate_steps)):
        result[1].append(intermediate_steps[i][0])
      return result
    else:
      intermediate_steps.append(next_step)


def convergent(cont_frac, index):
  cont_frac_no_period = cont_frac[0]
  while len(cont_frac_no_period) < index:
    cont_frac_no_period.extend(cont_frac[1])
  num = cont_frac_no_period[index - 1]
  den = 1
  for i in range(index-2, -1, -1):
    num, den = den + cont_frac_no_period[i] * num, num
  return num, den


def minimal_solution(D):
  cont_frac = continued_fraction_root(D)
  index = 1
  while True:
    x, y = convergent(cont_frac, index)
    if x**2 - D*y**2 == 1:
      return x, y
    index += 1


largest_D = 0
largest_x = 0
for D in range(2, 1001):
  if round(math.sqrt(D))**2 == D:
    continue

  x, y = minimal_solution(D)
  print("D = %i: minimal solution is %i^2 - %i * %i^2 = 1." % (D, x, D, y))
  if x > largest_x:
    largest_x = x
    largest_D = D

print("Largest x was at D = %i with x = %i" % (largest_D, largest_x))