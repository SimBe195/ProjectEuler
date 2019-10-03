import string

with open("p042_words.txt", "r") as f:
  file_string = f.read()
  file_string = file_string.replace("\"", "")
  words = file_string.split(",")


# print(max([len(word) for word in words]))
# The maximum word length is 14, so the maximum alphabetical value is 14*26 = 364.


def triangle_numbers_less_than(n):
  result = []
  k = 1
  t_k = 1
  while t_k <= n:
    result.append(t_k)
    k += 1
    t_k = int(k * (k+1) / 2)

  return result


triangle_numbers = triangle_numbers_less_than(364)
print(triangle_numbers)

triangle_words = []
for word in words:
  if sum([ord(c) - 64 for c in word]) in triangle_numbers:
    triangle_words.append(word)

print(triangle_words)
print(len(triangle_words))
