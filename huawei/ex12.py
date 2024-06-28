# 18. Write a NumPy program to find common values between two arrays.
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [10, 30, 40]
# Common values between two arrays:
# [10 40]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-18.php
import numpy as np

if __name__=='__main__':
    a = [0, 10, 20, 40, 60]
    b = [10, 30, 40]
    print(np.intersect1d(a,b))
