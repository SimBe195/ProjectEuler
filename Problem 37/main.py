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


def left_truncations(N):
  num_string = str(N)
  result = [N]
  result.extend([int(num_string[i:]) for i in range(1, len(num_string))])
  return result


def right_truncations(N):
  num_string = str(N)
  result = [N]
  result.extend([int(num_string[:-i]) for i in range(1, len(num_string))])
  return result


truncatable_primes = []
max_checked = 1000000
prime_checklist, primes = sieve_of_eratosthenes(max_checked)

for p in primes:
  if p <= 7:
    continue

  if all([prime_checklist[n] for n in left_truncations(p)]) and all([prime_checklist[n] for n in right_truncations(p)]):
    truncatable_primes.append(p)

  if len(truncatable_primes) == 11:
    break

print(truncatable_primes)
print(sum(truncatable_primes))
