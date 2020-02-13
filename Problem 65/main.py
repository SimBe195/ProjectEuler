import math


def continued_fraction(x, max_length=10):  # returns the continued fraction of arbitrary number x up to max_length
  intermediate_steps = [(int(x), 1 / (x - int(x)))]

  for i in range(max_length - 1):
    num = intermediate_steps[-1][1]
    next_a = int(num)
    next_step = (next_a, 1 / (num - next_a))
    intermediate_steps.append(next_step)

  result = []
  for step in intermediate_steps:
    result.append(step[0])
  return result


def convergent(cont_frac, index):
  num = cont_frac[index - 1]
  den = 1
  for i in range(index-2, -1, -1):
    num, den = den + cont_frac[i] * num, num
  return num, den


# e_frac = continued_fraction(math.e, 100) # not precise enough

e_frac = [1]*100
e_frac[0] = 2
for k in range(2, 100, 3):
  e_frac[k] = int(2*(k+1) / 3)
print(e_frac)

num, den = convergent(e_frac, 100)
sum_numerator_digits = sum([int(c) for c in str(num)])
print("The 100th convergent for e is %i / %i. Sum of the numerator-digits is %i" % (num, den, sum_numerator_digits))