import itertools


def property_fulfilled(n):
  num_string = str(n)
  if not int(num_string[1:4]) % 2 == 0:
    return False
  if not int(num_string[2:5]) % 3 == 0:
    return False
  if not int(num_string[3:6]) % 5 == 0:
    return False
  if not int(num_string[4:7]) % 7 == 0:
    return False
  if not int(num_string[5:8]) % 11 == 0:
    return False
  if not int(num_string[6:9]) % 13 == 0:
    return False
  if not int(num_string[7:10]) % 17 == 0:
    return False

  return True


solutions = []
digits = [str(i) for i in range(0, 10)]
for perm in itertools.permutations(digits):
  num_string = ""
  for digit in perm:
    num_string += digit

  num = int(num_string)
  if property_fulfilled(num):
    solutions.append(num)

print(solutions)
print(sum(solutions))