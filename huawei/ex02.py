# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-5.php

import numpy as np

if __name__=='__main__':
    a = np.arange(12, 38, 1)
    print(a)