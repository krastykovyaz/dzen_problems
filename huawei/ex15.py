# 25. Write a NumPy program to construct an array by repeating.

# Sample array: [1, 2, 3, 4]
# Expected Output:
# Original array
# [1, 2, 3, 4]
# Repeating 2 times
# [1 2 3 4 1 2 3 4]
# Repeating 3 times
# [1 2 3 4 1 2 3 4 1 2 3 4]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-25.php

import numpy as np

if __name__=='__main__':
    a = np.random.randint(2,10,3)
    print(np.tile(a,2),np.repeat(a,2))