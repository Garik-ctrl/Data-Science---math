import numpy as np
A = np.array([[3, 4, 5], [1, 2, 3], [4, 5, 6]])
B = np.array([[-2, 5, 1], [7, 0, 2], [-1, 0, 5]])

print(A + B)
print(A - B)
print(A * B) # po prvcích násobení
print(np.matmul(A, B)) # maticové násobení
print(A.T)

print(A.diagonal()) # prvky na diagonále
print(A.trace()) #suma na diagonále
print(A.flatten()) # zpět z matice na vektor


"""
TASK 1.7
Create the 4x4 matrix below, then:

display the item from the second row and the third column,
calculate its determinant,
calculate its trace (the sum of elements on the main diagonal),
find the largest and smallest item.
"""

matrix=np.random.randint(1,100,16).reshape(4, 4) #Create the 4x4 matrix below
print(matrix[1, 2])  #display the item from the second row and the third column,
print("Determinant ",np.linalg.det(matrix))  #calculate its determinant,
print("Trace ",np.trace(matrix)) #calculate its trace (the sum of elements on the main diagonal),
print("Největší prvek v matici:", np.max(matrix)) 
print("Nejmenší prvek v matici:", np.min(matrix))

"""
TASK 1.8
Print out all natural numbers less than 100 that are divisible by 11. 
Try not to use any iteration over loop.
"""

delitelne11 = np.arange(11, 100, 11)
print(delitelne11)

"""
TASK 1.10
Define two 3x3 real matrices, ie. whose elements consist entirely of real numbers. 
For the first matrix, draw the numbers from standard normal 
(Gaussian) distribution, ie.  μ=0  and  σ=1 . 
For the second one, set the standard devation to 1 (σ=1) and mean value to 5 (μ=0).
"""

matrix1=np.random.normal(loc=0,scale=1,size=(3,3)).round(2)
print(matrix1)
print("Vynásobeno 10: ", 10*matrix1)
print("Element uprostřed: ", matrix1[1,1])
print("Transponovaná matice: ", matrix1.T)
print("Trace: ", np.trace(matrix1))
print("Suma: ", np.sum(matrix1))
print("Suma: ", matrix1.sum())

"""
and calculate their:
sum
difference
element-wise multiplication result
element-wise division result
matrix product (matrix multiplication)
"""
matrix3=np.random.normal(loc=0,scale=1,size=(3,3)).round(2)
matrix4=np.random.normal(loc=0,scale=1,size=(3,3)).round(2)
print("Suma ",matrix3+matrix4)
print("difference ",matrix3-matrix4)
print("element-wise multiplication result ",matrix3*matrix4)
print("element-wise division result ",matrix3/matrix4)
print("(matrix multiplication) ",np.matmul(matrix3, matrix4))

# inverzní matice
A = np.array([
[1, 1],
[2, -1]
])
print("determinat ",np.linalg.det(A))
A_inv = np.linalg.inv(A)
print("Matice inverzní", A_inv)

print(np.matmul(A, A_inv).round(2))

#singulární matice
A = np.array([
[1, -0.5],
[-2, 1]
])
print(np.linalg.det(A))
print("Matice inverzní",np.linalg.inv(A))

"""
TASK 1.22
vyřešení soustavy tří rovnic 
C.X=D
x=C^-1.D
"""
C = np.array([
[1, -2,3],
[-1, 3,-1],
[2, -5,5]
])
print(C)
D=np.array([ 
[9], [-6], [17]
])
print(D)

C_inv = np.linalg.inv(C)
print(np.matmul( C_inv,D).round(2))
"""
TASK 1.23
vyřešení soustavy tří rovnic 
C.X=D
x=C^-1.D
"""
C = np.array([
[1, 1,1],
[6, -4,5],
[5, 2,2]
])
print(C)
D=np.array([
[2], [31], [13]
])
print(D)

C_inv = np.linalg.inv(C)
print(np.matmul( C_inv,D).round(2))
