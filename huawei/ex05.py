# Write a NumPy program to add a border (filled with 0's) around an existing array.
# Expected Output:
# Original array:
# [[ 1. 1. 1.]
# [ 1. 1. 1.]
# [ 1. 1. 1.]]
# 1 on the border and 0 inside in the array
# [[ 0. 0. 0. 0. 0.]
# ...........
# [ 0. 0. 0. 0. 0.]]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-9.php
import numpy as np


if __name__=='__main__':
    a = np.ones((5,5))
    print(np.pad(a, pad_width=1, mode='constant', constant_values=0))