
def digit_sum(n):
  return sum([int(c) for c in str(n)])

max_a = 0
max_b = 0
max_digit_sum = 1

for a in range(100):
  for b in range(100):
    digit_sum_a_to_b = digit_sum(a**b)
    if digit_sum_a_to_b > max_digit_sum:
      max_digit_sum = digit_sum_a_to_b
      max_a = a
      max_b = b

print("%i^%i has maximum digit sum %i" % (max_a, max_b, max_digit_sum))
