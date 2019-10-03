'''
  The product can't have 3 or less digits since the factors would be too large.
  The product also can't have 5 or more digits since then only four digits would be left for the factors but even
  99*99 < 10000, so this is not enough.
  => The product must have 4 digits. Then obviously also one of the factors has 2 or less digits.
'''

def digits(n):
  d = [int(i) for i in str(n)]
  d.sort()
  return d

sum_prods = 0

for prod in range(1000, 10000):
  prod_digits = digits(prod)

  if 0 in prod_digits:
    continue

  different_digits = True
  for i in range(len(prod_digits)-1):
    if prod_digits[i] == prod_digits[i+1]:
      different_digits = False
      break

  if not different_digits:
    continue

  remaining_digits = [n for n in range(1, 10) if n not in prod_digits]
  for a in range(1, 100):
    if not prod % a == 0:
      continue

    a_digits = digits(a)

    if any([d not in remaining_digits for d in a_digits]):
      continue

    if a > 9 and len(a_digits) < 2:
      continue

    b_available_digits = [n for n in remaining_digits if n not in a_digits]

    b = prod // a
    if b_available_digits == digits(b):
      print("%i * %i = %i" % (a, b, prod))
      sum_prods += prod
      break

print(sum_prods)
