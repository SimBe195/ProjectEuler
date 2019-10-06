
counter = 0
for n in range(23, 101):
  n_over_r = 1
  for r in range(1, int(n/2) + 1):
    n_over_r = int(n_over_r * (n-r+1) / r)
    if n_over_r > 1000000:
       counter += (n+1) - (2*r)
       break

print(counter)
