import math
import itertools


def sort_digits(n):
  digit_list = list(str(n))
  digit_list.sort()
  sort_string = ""
  for d in digit_list:
    sort_string += d
  return sort_string


num_occurrences_of_permutations = {}

n = 1
while True:
  n += 1
  cube = n**3
  sorted_digits = sort_digits(cube)
  if sorted_digits in num_occurrences_of_permutations:
    num_occurrences_of_permutations[sorted_digits][0] += 1
  else:
    num_occurrences_of_permutations[sorted_digits] = [1, cube]

  if num_occurrences_of_permutations[sorted_digits][0] == 5:
    print("Smallest cube with 5 permutation cubes is %s." % num_occurrences_of_permutations[sorted_digits][1])
    break
