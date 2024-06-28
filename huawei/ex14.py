# 20. Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2.
# Expected Output:
# Array1: [ 0 10 20 40 60 80]
# Array2: [10, 30, 40, 50, 70, 90]
# Set difference between two arrays:
# [ 0 20 60 80]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-20.php

import numpy as np

if __name__=='__main__':
    a = np.random.randint(2,5, 4)
    b = np.random.randint(2,5, 4)
    print(a,b)
    print(np.setdiff1d(a,b))