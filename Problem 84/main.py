import numpy as np
from fractions import Fraction
import time
tic = time.perf_counter()
"""
  We can model the game using Markov Chains. For each of the 40 squares we introduce 3 states into the graph, to model
  whether we arrived there after no double, after one double or after two consecutive doubles.
  After constructing the matrix of transition probabilities we can get a stable distribution as an eigenvector to
  eigenvalue 1.
  Also for accuracy first construct the transition matrix using fractions and convert to floats later.
"""

def square_to_idx(square, doubles):
  return 3*square + doubles

def idx_to_square(idx):
  return np.floor(idx/3), idx % 3


# Model dice-roll probabilities by a dict with (roll-value, double) as key and the probability as value

# 2x 6-sided:
# roll_probs = {(2, True):   Fraction(1, 36),
#               (3, False):  Fraction(2, 36),
#               (4, True):   Fraction(1, 36),
#               (4, False):  Fraction(2, 36),
#               (5, False):  Fraction(4, 36),
#               (6, True):   Fraction(1, 36),
#               (6, False):  Fraction(4, 36),
#               (7, False):  Fraction(6, 36),
#               (8, True):   Fraction(1, 36),
#               (8, False):  Fraction(4, 36),
#               (9, False):  Fraction(4, 36),
#               (10, True):  Fraction(1, 36),
#               (10, False): Fraction(2, 36),
#               (11, False): Fraction(2, 36),
#               (12, True):  Fraction(1, 36)}

# 2x 4-sided:
roll_probs = {(2, True):  Fraction(1, 16),
              (3, False): Fraction(2, 16),
              (4, True):  Fraction(1, 16),
              (4, False): Fraction(2, 16),
              (5, False): Fraction(4, 16),
              (6, True):  Fraction(1, 16),
              (6, False): Fraction(2, 16),
              (7, False): Fraction(2, 16),
              (8, True):  Fraction(1, 16)}

transition_matrix = np.empty((120, 120), dtype=np.object)
for x in range(120):
  for y in range(120):
    transition_matrix[x, y] = Fraction(0, 1)


def chance(square, double, source, base_prob):
  transition_matrix[square_to_idx(square, double), source] += base_prob * Fraction(14, 16)
  transition_matrix[square_to_idx(0, double), source] += base_prob * Fraction(1, 16)  # Advance to Go
  transition_matrix[square_to_idx(10, double), source] += base_prob * Fraction(1, 16)  # Go to jail


def community(square, double, source, base_prob):
  next_r = 0
  next_u = 0
  if target_square == 7:
    next_r = 15
    next_u = 12
  elif target_square == 22:
    next_r = 25
    next_u = 28
  elif target_square == 36:
    next_r = 5
    next_u = 12

  transition_matrix[square_to_idx(square, double), source] += base_prob * Fraction(6, 16)
  transition_matrix[square_to_idx(0, double), source] += base_prob * Fraction(1, 16)  # Advance to go
  transition_matrix[square_to_idx(10, double), source] += base_prob * Fraction(1, 16)  # Go to jail
  transition_matrix[square_to_idx(11, double), source] += base_prob * Fraction(1, 16)  # Go to C1
  transition_matrix[square_to_idx(24, double), source] += base_prob * Fraction(1, 16)  # Go to E3
  transition_matrix[square_to_idx(39, double), source] += base_prob * Fraction(1, 16)  # Go to H2
  transition_matrix[square_to_idx(5, double), source] += base_prob * Fraction(1, 16)  # Go to R1
  transition_matrix[square_to_idx(next_r, double), source] += base_prob * Fraction(2, 16)  # Go to next R
  transition_matrix[square_to_idx(next_u, double), source] += base_prob * Fraction(1, 16)  # Go to next U

  # Go back 3 squares has to be handled carefully: you can go from 36 to 33 (chance)
  if square == 36:
    chance(33, double, source, base_prob * Fraction(1, 16))
  else:
    transition_matrix[square_to_idx(square - 3, target_double), source] += base_prob * Fraction(1, 16)


for square in range(40):
  for double in range(3):
    source_idx = square_to_idx(square, double)
    for roll, prob in roll_probs.items():
      target_square = (square + roll[0]) % 40

      # go straight to jail after the third double
      if roll[1]:
        if double == 2:
          transition_matrix[square_to_idx(10, 0), source_idx] += prob
          continue
        else:
          target_double = double + 1
      else:
        target_double = 0

      if target_square in [2, 17, 33]:  # cc squares
        chance(target_square, target_double, source_idx, prob)
      elif target_square in [7, 22, 36]:  # ch squares
        community(target_square, target_double, source_idx, prob)
      elif target_square == 30:  # Go to jail
        transition_matrix[square_to_idx(10, 0), source_idx] += prob
      else:  # Normal square
        transition_matrix[square_to_idx(target_square, target_double), source_idx] += prob

transition_matrix = transition_matrix.astype(np.float)

w, v = np.linalg.eig(transition_matrix)
eigenvec = v[:, 0] / np.sum(v[:, 0])
eigenvec = eigenvec.real

summed_v = np.array([np.sum(eigenvec[3*i:3*(i+1)]) for i in range(40)])
# print("Square probabilities: ", summed_v)
print("Most popular squares: ")
ranking = np.flip(np.argsort(summed_v))
for i in range(3):
  print("%i: %.2f" % (ranking[i], 100*summed_v[ranking[i]].real))

print("Runtime: %.2f ms" % ((time.perf_counter() - tic) * 1000))