# 12. Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array:
# [10, 20, 30]
# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-12.php
import numpy as np

if __name__=='__main__':
    a = [10, 20, 30]
    print(np.append(a, [60, 70, 80, 90]))
