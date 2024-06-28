# 11. Write a NumPy program to convert a list and tuple into arrays.
# List to array:
# [1 2 3 4 5 6 7 8]
# Tuple to array:
# [[8 4 6]
# [1 2 3]]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-11.php

import numpy as np

if __name__=='__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    a = np.asarray(l)
    t = ([1, 2, 3], [6, 7, 8])
    b = np.asarray(t)
    print(a, b)
