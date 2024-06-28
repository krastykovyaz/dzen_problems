# 3.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-3.php
import numpy as np

if __name__=='__main__':
    a = [[ 2, 3, 4], \
        [ 5, 6, 7], \
        [ 8, 9, 10]]
    print(np.sort(np.array(a)))

