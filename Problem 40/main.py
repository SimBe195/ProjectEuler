'''
Index-range of 1-digit-numbers: 1 - 9
Index-range of 2-digit-numbers: 10 - 9 + 2*90 -> 10 - 189
Index-range of 3-digit-numbers: 190 - 189 + 3*900 -> 190 - 2889
...
'''

index_ranges = []
last_max = 0
n = 1
while last_max < 1000000:
  next_start = last_max + 1
  next_end = last_max + n * 9 * (10 ** (n-1))
  index_ranges.append((next_start, next_end))
  last_max = next_end
  n += 1

prod = 1
for n in range(7):
  digit_num = 10**n
  range_index = 0
  while index_ranges[range_index][1] < digit_num:
    range_index += 1

  r = index_ranges[range_index]

  number = int(10 ** range_index) + int((digit_num - r[0]) / (range_index + 1))
  index_in_number = (digit_num - r[0]) % (range_index + 1)
  prod *= int(str(number)[index_in_number])
  print(digit_num, r, number, index_in_number)

print(prod)
