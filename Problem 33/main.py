import math


def first_digit(num):
  return int(str(num)[0])


def second_digit(num):
  return int(str(num)[1])


def reduced_fractions(frac):
  results = []
  a_1 = first_digit(frac.numerator)
  a_2 = second_digit(frac.numerator)
  b_1 = first_digit(frac.denominator)
  b_2 = second_digit(frac.denominator)

  if a_1 == b_1 and b_2 != 0:
    results.append(Fraction(a_2, b_2))

  if a_1 == b_2 and b_1 != 0:
    results.append(Fraction(a_2, b_1))

  if a_2 == b_1 and b_2 != 0:
    results.append(Fraction(a_1, b_2))

  if a_2 == b_2 and b_1 != 0:
    results.append(Fraction(a_1, b_1))

  return results


class Fraction:
  numerator = 0
  denominator = 1

  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def equal(self, frac2):
    return self.numerator * frac2.denominator == self.denominator * frac2.numerator

  def __str__(self):
    return "%i / %i" % (self.numerator, self.denominator)


solutions = []
for a in range(10, 100):
  for b in range(a+1, 100):
    if a == b:
      continue

    a_over_b = Fraction(a, b)
    for frac in reduced_fractions(a_over_b):
      if a_over_b.numerator == 10 * frac.numerator:
        continue # trivial example
      if a_over_b.equal(frac):
        solutions.append((a_over_b, frac))

for sol in solutions:
  print(str(sol[0]), "; ", str(sol[1]))

prod_num = 1
prod_den = 1

for sol in solutions:
  prod_num *= sol[0].numerator
  prod_den *= sol[0].denominator

d = math.gcd(prod_num, prod_den)
prod_num = int(prod_num / d)
prod_den = int(prod_den / d)

print(prod_num, prod_den)
