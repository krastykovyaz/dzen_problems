# 19. Write a NumPy program to get the unique elements of an array.
# Expected Output:
# Original array:
# [10 10 20 20 30 30]
# Unique elements of the above array:
# [10 20 30]
# Original array:
# [[1 1]
# [2 3]]
# Unique elements of the above array:
# [1 2 3]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-19.php

import numpy as np

if __name__=='__main__':
    a = np.array([10, 10, 20, 20, 30, 30])
    b = np.array([[1, 1], [2, 3]])
    print(np.unique(a), np.unique(b))