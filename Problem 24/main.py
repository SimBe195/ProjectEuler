import numpy as np
from functools import reduce

'''
  The first 9! = 362.880 permutations start with digit 0.
  The next 362.880 permutations start with digit 1.
  The millionth permutation starts with digit 2, it is the 1000000 - 2*362800 = 274.240th permutation starting with a 2.
  8! = 40.320, so there are 40.320 permutations with 0 as its second digit, 40.320 with 1 and so on. In this way we can find the second digit.
  And so on.
'''


def factorial(n):
  return np.prod(range(2, n+1))


target_permutation_index = 999999
digit_sequence = []
remaining_digits = list(range(10))
n_fact = factorial(len(remaining_digits))

while not len(remaining_digits) == 0:
  n_fact /= len(remaining_digits)
  current_digit_index = int(target_permutation_index / n_fact)
  target_permutation_index %= n_fact

  current_digit = remaining_digits[current_digit_index]
  digit_sequence.append(current_digit)
  remaining_digits.remove(current_digit)

print(reduce((lambda x, y: str(x) + str(y)), digit_sequence))
