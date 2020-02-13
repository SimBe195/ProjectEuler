import math

"""
  Similar to problem 76 but use a list instead of recursion, since we want to generate all partition values until we
  reach our goal.
  Also we can do all calculations modulo 1,000,000 to avoid huge numbers
"""

p = [1]
n = 0
while True:
  n += 1

  sub_sum = 0
  for k in range(math.ceil(-(math.sqrt(24 * n + 1) - 1) / 6), math.floor((math.sqrt(24 * n + 1) + 1) / 6 + 1)):
    if k == 0:
      continue
    if k % 2 == 0:
      sign = -1
    else:
      sign = 1
    sub_sum += sign * p[n - int(k * (3 * k - 1) / 2)] % 1000000
  p.append(sub_sum % 1000000)
  if p[n] % 1000000 == 0:
    print("For n = %i, p(n) is divisible by 1,000,000." % n)
    break
