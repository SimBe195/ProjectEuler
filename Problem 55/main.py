

def reverse_number(n):
  digits = list(str(n))
  rev_digits = digits[::-1]
  rev_string = ""
  for digit in rev_digits:
    rev_string += digit
  return int(rev_string)


def num_steps(n, max_steps=50):  # if more than max_steps steps are needed, this function returns max_steps
  k = 1
  current_num = n + reverse_number(n)
  while k < max_steps:
    rev_num = reverse_number(current_num)
    if rev_num == current_num:
      return k
    k += 1
    current_num += rev_num

  return max_steps


max_steps = 50
counter = 0
for n in range(10000):
  steps = num_steps(n, max_steps)
  if steps == max_steps:
    print("%i is a Lychrel number" % n)
    counter += 1


print(counter)
