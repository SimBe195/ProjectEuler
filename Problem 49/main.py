
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


def are_permutations(n_1, n_2):
  n_1_digits = list(str(n_1))
  n_1_digits.sort()
  n_2_digits = list(str(n_2))
  n_2_digits.sort()
  return n_1_digits == n_2_digits


for p in primes:
  if p < 1000:
    continue

  if p == 1487:
    continue

  sol_found = False
  for k in range(1, int((10000 - p) / 2)):
    if not prime_checklist[p+k] or not prime_checklist[p + 2*k]:
      continue
    if are_permutations(p, p+k) and are_permutations(p, p+2*k):
      print("Solution %i, %i, %i found." % (p, p+k, p+2*k))
      print("Concatenation: {}".format(str(p) + str(p+k) + str(p+2*k)))
      sol_found = True
      break

  if sol_found:
    break

