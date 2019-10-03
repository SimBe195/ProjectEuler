
num_list = []

for a in range(2, 101):
  for b in range(2, 101):
    a_to_b = a**b
    if a_to_b not in num_list:
      num_list.append(a_to_b)

print(len(num_list))