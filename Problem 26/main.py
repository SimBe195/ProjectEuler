"""
in general a number 0.a_1 a_2 a_3 ... a_k (a_k+1 ... a_l)^- can be written as the fraction
[ a_1 ... a_k * (10^(l-k) - 1) + a_k+1 ... a_l ] / [10^l - 10^k]
So if the decimal expansion of some fraction 1/x has a recurring cycle of length n then
1 / x = a / (10^k * (10^n - 1)) for some a, k.
This leads to the condition x | 10^k * (10^n - 1). So the recurring cycle length of 1/x
is precisely the smallest n for which there is a value of k such that this condition is fulfilled. Since 10^n - 1 does not have
prime factors 2 and 5, which on the other hand are the only prime factors of 10^k, we can write x = 2^a * 5^b * y for a y with
gcd(y,2) = gcd(y,5) = 1. Then n is simply the smallest number for which y divides 10^n-1 and we don't have to worry about k anymore.
"""


def p_exponent(n, p):
  exponent = 0
  while n % p == 0:
    exponent += 1
    n /= p
  return exponent


def len_rec_cycle(n):
  y = n // 2**p_exponent(n, 2) // 5**p_exponent(n, 5)

  if y == 1:
    return 0

  exp = 1
  while True:
    if (10**exp - 1) % y == 0:
      return exp
    exp += 1


max_len = 0
max_num = 0
for n in range(1, 1001):
  len_n = len_rec_cycle(n)

  if len_n > max_len:
    max_len = len_n
    max_num = n

print(max_num)
print(max_len)
