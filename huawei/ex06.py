# 10. Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.
# Checkerboard pattern:
# [[0 1 0 1 0 1 0 1]
# ..........
# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-10.php
import numpy as np

if __name__=='__main__':
    a = np.zeros((8, 8), dtype=int)
    a[1::2, ::2]=1
    a[::2, 1::2]=1
    print(a)