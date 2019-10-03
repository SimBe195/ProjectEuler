
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


def num_digits(N):
  return len(str(N))


def circle(N):
  results = []
  n_string = str(N)
  for i in range(num_digits(N)):
    circle_number = int(n_string[i:] + n_string[0:i])
    if circle_number not in results:
      results.append(circle_number)

  return results


prime_checklist, primes = sieve_of_eratosthenes(1000000)
solutions = []
for p in primes:
  circle_p = circle(p)
  if all([prime_checklist[x] for x in circle_p]):
    solutions.extend(circle_p)
    circle_p.remove(p)
    for x in circle_p:
      primes.remove(x)

print(solutions)
print(len(solutions))