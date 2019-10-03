def sieve_of_eratosthenes(N):
  prime_checklist = [True] * (N + 1)
  prime_checklist[0] = False
  prime_checklist[1] = False
  for n in range(2, N + 1):
    if not prime_checklist[n]:
      continue
    for k in range(2 * n, N + 1, n):
      prime_checklist[k] = False

  return prime_checklist, [n for n in range(N + 1) if prime_checklist[n]]


def zero_pad(string, length):
  return "0"*(length - len(string)) + string


def subsets(n): # returns list of subsets of {0, ..., n-1}, except for the empty set
  result = []
  for x in range(1, 2**n):
    bin_string = zero_pad(str(bin(x))[2:], n)
    result.append([i for i in range(n) if bin_string[i] == '1'])

  return result


def num_digits(n):
  return len(str(n))


def replace_digits(n, index_set, digit):
  num_string = str(n)
  digit_string = str(digit)
  for index in index_set:
    num_string = num_string[:index] + digit_string + num_string[index+1:]
  return int(num_string)


prime_checklist, primes = sieve_of_eratosthenes(1000000)
prime_found = False

for p in primes:
  if prime_found:
    break
  for set in subsets(num_digits(p)):
    prime_replacements = []

    digit_range = range(10)
    if 0 in set:
      digit_range = range(1, 10)

    for digit in digit_range:
      x = replace_digits(p, set, digit)
      if prime_checklist[x]:
        prime_replacements.append(x)

    if len(prime_replacements) >= 8:
      print("number", p, "index-set", set, "replacements", prime_replacements)
      prime_found = True
      break

