# 6. Write a NumPy program to reverse an array (the first element becomes the last).
# Original array:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
# Reverse array:
# [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-6.php
import numpy as np

if __name__=='__main__':
    a = np.arange(12,38)
    print(a[::-1])
