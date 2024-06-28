# 14. Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91]
# [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees:
# [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees:
# [-0. 12. 45.21 34. 99.91 32. ]
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-14.php
import numpy as np

if __name__=='__main__':
    vals = np.array([0, 12, 45.21, 34, 99.91, 32])
    print(np.round((5 * vals / 9 - 5 * 32 / 9), 2))