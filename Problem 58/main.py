import math


def diagonal_numbers(index): # innermost spiral (1) is said to have index 0
  min_in_spiral = (2*index-1)**2 + 1
  side_length = 2 * index + 1
  diag_nums = [min_in_spiral + side_length - 2]
  for i in range(1, 4):
    diag_nums.append(diag_nums[-1] + side_length - 1)
  return diag_nums


def is_prime(n):

  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True


count_primes = 0
count_total = 1

index = 1
while True:
  diag_nums = diagonal_numbers(index)
  for num in diag_nums:
    if is_prime(num):
      count_primes += 1
  count_total += 4

  if count_primes * 10 < count_total:
    print("Index %i is the first with less than 10 percent primes on the diagonals." % index)
    print("It corresponds to side_length %i" % (2*index+1))
    break

  index += 1