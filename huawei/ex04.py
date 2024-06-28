# 8. Write a NumPy program to create a 2D array with 1 on the border and 0 inside.
# Expected Output:
# Original array:
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]
# 1 on the border and 0 inside in the array
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-8.php
import numpy as np


if __name__=='__main__':
    a = np.ones((5,5))
    a[1:-1,1:-1] = 0
    print(a)