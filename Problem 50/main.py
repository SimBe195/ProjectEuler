
'''
  We use an array S containing the cumulative sum of all primes 2 = p_1, 3 = p_2, ..., p_i in index i. Then the sum of
  consecutive primes p_i, ..., p_j is just S[j] - S[i-1]. So we have to find number i, j for which S[j] - S[i-1] is a prime
  < 1,000,000 and j - i is maximal.
'''

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
cumulative_prime_sums = [2]
for p in primes[1:]:
  cumulative_prime_sums.append(cumulative_prime_sums[-1] + p)


max_prime = 0
max_len = 0
for j in range(len(cumulative_prime_sums)):
  for i in range(j, -1, -1):
    if i == 0:
      diff = cumulative_prime_sums[j]
    else:
      diff = cumulative_prime_sums[j] - cumulative_prime_sums[i - 1]

    if diff >= 1000000:
      break
    if prime_checklist[diff]:
      l = j - (i-1)
      if l > max_len:
        print("New maximum: %i is the sum of %i consecutive primes" % (diff, l))
        max_prime = diff
        max_len = l

print(max_prime, max_len)