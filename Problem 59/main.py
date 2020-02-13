
with open("p059_cipher.txt", "r") as f:
  content = f.read()

values = [int(c) for c in content.split(",")]


def values_to_text(value_array):
  characters = [chr(i) for i in value_array]
  text = ""
  for c in characters:
    text += c
  return text


def is_english_text(text):
  num_words = len(text.split(" "))
  if num_words*10 < len(text):
    return False
  text_low = text.lower()
  common_words = ["the", "be", "to", "of", "and", "a", "in"]
  if all([word in text_low for word in common_words]):
    return True
  return False


def apply_key(key):
  result = []
  for i in range(len(values)):
    result.append(values[i] ^ key[i % len(key)])

  return result


for char_1 in range(97, 123): # 97 = 'a', 122 = 'z'
  for char_2 in range(97, 123):
    for char_3 in range(97, 123):
      key = [char_1, char_2, char_3]
      candidate_values = apply_key(key)
      candidate_text = values_to_text(candidate_values)
      if is_english_text(candidate_text):
        print("Candidate key {} found! Text is {}".format(key, candidate_text))
        print("Sum is %i" % sum(candidate_values))


