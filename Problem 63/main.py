'''
For x >= 10: x^n >= 10^n  which is a (n+1)-digit number, so we only have to check x^n for x in {1,...,9}.
For these numbers, if x^n has less than n digits, x^{n+1} can't have n+1 digits, so once this condition is fulfilled,
there can be no more n-digit numbers x^n for larger n.
'''


def num_digits(n):
  return len(str(n))


nums = []
for x in range(1, 10):
  power = 1
  num = x
  while True:
    if num_digits(num) == power:
      if num not in nums:
        nums.append(num)
    else:
      break
    power += 1
    num *= x

print(nums)
print(len(nums))