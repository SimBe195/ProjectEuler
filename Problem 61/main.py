import itertools

def triangle_number(n):
  return int(n * (n+1) / 2)


def square_number(n):
  return int(n * n)


def pentagonal_number(n):
  return int(n * (3*n - 1) / 2)


def hexagonal_number(n):
  return int(n * (2*n - 1))


def heptagonal_number(n):
  return int(n * (5*n - 3) / 2)


def octagonal_number(n):
  return int(n * (3*n - 2))


def four_digit_values(function):
  result = []
  n = 0
  while True:
    p_n = function(n)
    if p_n >= 10000:
      break
    if p_n >= 1000:
      result.append(p_n)
    n += 1

  return result


tri = four_digit_values(triangle_number)
squ = four_digit_values(square_number)
pent = four_digit_values(pentagonal_number)
hex = four_digit_values(hexagonal_number)
hept = four_digit_values(heptagonal_number)
oct = four_digit_values(octagonal_number)


def first_digits(number):
  return int(str(number)[:2])


def last_digits(number):
  return int(str(number)[2:])


def number_of_odd_frequencies(number_list): # returns, how many two digit numbers appear an odd number of times at the start or end of numbers in the list
  two_digit_parts = []
  for n in number_list:
    first = first_digits(n)
    if first in two_digit_parts:
      two_digit_parts.remove(first)
    else:
      two_digit_parts.append(first)

    last = last_digits(n)
    if last in two_digit_parts:
      two_digit_parts.remove(last)
    else:
      two_digit_parts.append(last)

  return len(two_digit_parts)


def cyclical(number_list):
  for i in range(len(number_list) - 1):
    if last_digits(number_list[i]) != first_digits(number_list[i+1]):
      return False

  return first_digits(number_list[0]) == last_digits(number_list[-1])


permutation_exists = False
for a in oct:
  if permutation_exists:
    break

  for b in hept:
    if permutation_exists:
      break

    for c in hex:
      if permutation_exists:
        break

      for d in pent:
        if permutation_exists:
          break
        number_list = [a, b, c, d]
        if number_of_odd_frequencies(number_list) > 4:
          continue

        for e in squ:
          if permutation_exists:
            break
          number_list = [a, b, c, d, e]
          if number_of_odd_frequencies(number_list) > 2:
            continue

          for f in tri:
            if permutation_exists:
              break

            number_list = [a, b, c, d, e, f]
            if number_of_odd_frequencies(number_list) > 0:
              continue

            for permutation in itertools.permutations(number_list):
              if cyclical(permutation):
                permutation_exists = True
                print(permutation)
                print(sum(permutation))
                break

