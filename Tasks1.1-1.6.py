# -*- coding: utf-8 -*-
import numpy as np

"""
Task 1.1.2
Create a NumPy array with consecutive values from 1 to 9. 
Display and then invert this array 
(first element becomes last, etc.).
"""
A=np.arange(7,20)
print(A)
B=A[::-1]
print(B)
print(A[::-1])

"""
Task 1.2.1
Create the following NumPy array: 
np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1]); 
and then list all unique (non-repeating) elements.
"""

C=np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1])
print(C)

D=np.unique(C)
print(D)

"""
Task 1.2.2
Create the following NumPy array: 
np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1]); 
and then list all unique (non-repeating) elements.
"""

E= np.array([44, 1, 7, 12, 7, 44, 4, 7, 12, 1])
print(E)

jedin, hodnoty =np.unique(E,return_counts=True)

print(jedin)
print(hodnoty)

"""
Task 1.3
Create a 3x3 matrix (by using reshape) with values between 2 and 10.
"""
F= np.arange(2,11).reshape(3, 3)
print(F)

"""
Task 1.4
Create an array with six random values between 10 and 30.
"""
random_array = np.random.randint(10,31,6)
print(random_array)

"""
Task 1.5
Use the following code to define 2D array, ie. matrix, and then determine its dimension and number of elements.
"""

G = np.array([[1, 2, 3, 4], [5, 6, -7, 1]])
print(f"Počet záznamů: {G.size}")
print(f"Počet rozměrů: {G.ndim}")
"""
Task 1.6
From the array of values: [23, 45, 112, 150, 43, 254, 95, 8] filter for those that are greater than 100.
"""
H=np.array([23, 45, 112, 150, 43, 254, 95, 8] )
print(H[H> 100])




