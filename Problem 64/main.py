import math

'''
  Let x be any number, then x = a + 1 / ( b / (x - c)) and we can continue developing the continued fraction
  by writing b / (x - c) in this form and so on.
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


counter = 0
for n in range(10001):
  if round(math.sqrt(n))**2 == n: # n is a square number
    continue
  cont_frac = continued_fraction_root(n)
  period_len = len(cont_frac[1])
  if period_len % 2 == 1:
    counter += 1

print(counter)



