# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-4.php
import numpy as np

if __name__=='__main__':
    a = np.zeros(10)
    a[6] = 11
    print(a)