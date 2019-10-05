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


prime_checklist, primes = sieve_of_eratosthenes(1000000)


def prime_decomposition(n):
  if n == 1:
    return {}

  dec = {}
  current = n
  for p in primes:
    if current == 1:
      return dec
    if prime_checklist[current]:
      dec[current] = 1
      return dec

    if current % p == 0:
      exp = 1
      current = int(current / p)
      while current % p == 0:
        exp += 1
        current = int(current / p)

      dec[p] = exp


num_conseq = 4
n = 1
decompositions = [prime_decomposition(k) for k in range(n, n+num_conseq)]
while True:
  shifted = False
  for i in range(num_conseq - 1, -1, -1):
    if len(decompositions[i]) != num_conseq:
      n += i + 1
      decompositions = decompositions[i+1:]
      decompositions.extend([prime_decomposition(k) for k in range(n + num_conseq - i - 1, n+num_conseq)])
      shifted = True
      break

  if shifted:
    continue

  print("Solution %i found!" % n)
  for k in range(n, n + num_conseq):
    print("{} = {}".format(k, decompositions[k - n]))
  break
