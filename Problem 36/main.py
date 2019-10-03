
def is_palindrome(num):
  num_string = str(num)
  return num_string == num_string[::-1]


def is_binary_palindrome(num):
  bin_num_string = str(bin(num))[2:]
  return bin_num_string == bin_num_string[::-1]


palindromes = []
for i in range(1000000):
  if is_palindrome(i) and is_binary_palindrome(i):
    palindromes.append(i)

print(palindromes)
print(sum(palindromes))