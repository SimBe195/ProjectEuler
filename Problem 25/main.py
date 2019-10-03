import numpy as np

'''
  An explicit formula for the n'th fibonacci number is F_n = ( phi^n - (-1/phi)^n ) / sqrt(5) for phi = (1 + sqrt(5)) / 2.
  The number of digits of F_n is therefore the ceiling of log_10 (F_n) = log_10 ( phi^n - (-1/phi)^n) ) - log_10(sqrt(5)).
  Since (-1/phi)^n quickly tends towards 0 for large n, and the n we are looking for is likely pretty large, we approximate
  log_10(F_n) ~ n * log_10(phi) - log_10(sqrt(5))
  The smallest n for which log_10(F_n) > 999 is therefore approximately the smallest n for which
  999 < n * log_10(phi) - log_10(sqrt(5))
  => n ~ 4782
  And indeed, 4782 is the first fibonacci number with 1000 digits.
'''

phi = (1 + np.sqrt(5)) / 2
print((999 + np.log10(np.sqrt(5))) / np.log10(phi))
