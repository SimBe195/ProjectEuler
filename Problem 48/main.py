
num_digits = 10

def power_mod_m(x, power, m):
  current = 1
  for k in range(power):
    current *= x
    current %= m
  return current


sum_powers = 0
modulus = 10**num_digits
for k in range(1, 1001):
  sum_powers += power_mod_m(k, k, modulus)
  sum_powers %= modulus

print(sum_powers)

