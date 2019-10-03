'''
  For an n-digit-number we get the condition 10^(n-1) <= a_1 a_2 ... a_n = a_1^5 + a_2^5 + ... + a_n^5 <= n*9^5
  => 10^(n-1) / n <= 9^5 = 59,049. This is not fulfilled for n >= 7, so we can only have numbers with a maximum of six digits.
'''

fifth_powers = [i**5 for i in range(10)]

sum_nums = 0
for n in range(2, 10000000):
  if n == sum([fifth_powers[int(i)] for i in str(n)]):
    print("%i can be written as the sum of fifth powers of its digits" % n)
    sum_nums += n

print(sum_nums)

