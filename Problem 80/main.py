from decimal import *

# 100 decimal digits + 1 for the integer part, + 1 for an additional digit at the end to prevent rounding
getcontext().prec = 102

digital_sum = 0
for n in range(1, 101):
  if n in [i*i for i in range(11)]:
    continue
  root = Decimal(n).sqrt()
  digital_sum += sum([int(x) for x in str(root)[0] + str(root)[2:-2]])

print(digital_sum)
