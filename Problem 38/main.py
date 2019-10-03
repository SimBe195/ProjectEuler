
def concat_product(integer, multipliers):
  products = [integer * i for i in range(1, multipliers+1)]
  concat_string = ""
  for product in products:
    concat_string += str(product)

  return int(concat_string)


def is_pandigital(integer):
  num_string = str(integer)
  digit_list = list(num_string)

  if len(num_string) != 9:
    return False
  for digit in range(1, 10):
    if not str(digit) in digit_list:
      return False

  return True


max_pandigital = 0
for integer in range(10000):  # integer can't be longer than 4 digits since we have at least 2 products with at least as many digits which are concatenated
  for n in range(2, int(9 / len(str(integer))) + 1): # can't repeat numbers of the length of the given integer more than 9/len times
    concat = concat_product(integer, n)
    if concat <= max_pandigital:
      continue
    if concat > 987654321:
      break

    if is_pandigital(concat):
      print("New maximum found: %i which is %i with (1,...,%i)" % (concat, integer, n))
      max_pandigital = concat

print(max_pandigital)