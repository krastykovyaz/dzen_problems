# 17. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [0, 40]
# Compare each element of array1 and array2
# [ True False False True False]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-17.php

import numpy as np

if __name__=='__main__':
    a = [0, 10, 20, 40, 60]
    b = [0, 40]
    print(np.in1d(a,b))