import math

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


prime_checklist, primes = sieve_of_eratosthenes(10000)
prime_checklist = {i: prime_checklist[i] for i in range(len(prime_checklist))}


def is_prime(n):
  if n in prime_checklist:
    return prime_checklist[n]

  for i in range(2, math.floor(math.sqrt(n))):
    if n % i == 0:
      prime_checklist[n] = False
      return False

  prime_checklist[n] = True
  return True


def next_prime(n):
  test_num = n + 1
  while not is_prime(test_num):
    test_num += 1

  return test_num


class SetOfPrimes: # contains a list of <size> different primes in ascending order
  def __init__(self, size):
    self.set = primes[:size]

  def next_set(self, start_index):
    index = start_index
    while index < len(self.set) - 1:
      next = next_prime(self.set[index])
      if next == self.set[index + 1]:
        index += 1
      else:
        self.set[index] = next
        break

    if index == len(self.set) - 1:
      self.set[-1] = next_prime(self.set[-1])

    self.set[:index] = primes[:index]


def concatenation(number_list, index1, index2):
  return int(str(number_list[index1]) + str(number_list[index2]))


size = 5
prime_set = SetOfPrimes(size)
while True:
  success = True
  for a in range(size-1, -1, -1):
    if not success:
      break
    for b in range(size-1, -1, -1):
      if a == b:
        continue
      if not is_prime(concatenation(prime_set.set, a, b)):
        prime_set.next_set(min(a, b))
        success = False
        break

  if success:
    print(prime_set.set)
    print(sum(prime_set.set))
    break