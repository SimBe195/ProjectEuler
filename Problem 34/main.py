
'''
If a_1 a_2 ... a_n is such a number, then 10^(n-1) <= a_1 a_2 ... a_n = a_1! + a_2! + ... + a_n! <= n*9!
=> 10^(n-1) / n <= 9! = 362,880.
This is not fulfilled for n >= 8, so we are looking for numbers with at most 7 digits.
'''

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def digit_factorial_sum(num):
  digits = [int(d) for d in str(num)]
  digit_factorials = [factorials[d] for d in digits]
  return sum(digit_factorials)


solutions = []

for n in range(3, 10000000):
  if n % 1000000 == 0:
    print(n)
  if n == digit_factorial_sum(n):
    print("solution %i found" % n)
    solutions.append(n)

print(sum(solutions))