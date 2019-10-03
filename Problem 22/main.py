import numpy as np

with open("p022_names.txt", "r") as f:
  text = f.read()
  text = text.replace("\"", "")
  names = text.split(",")
  names.sort()

  total = np.int64(0)
  for index, name in enumerate(names):
    alph_val = np.sum([ord(c) - 64 for c in name])
    total += (index + 1)*alph_val

print(total)
