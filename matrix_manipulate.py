import numpy as np

row = int(input("Please enter the no of rows"))
column = int(input("Please enter the number of columns"))

mat1 = []
mat2 = []
print("Please enter the value row-wise")

'''Here we are taking user input row wise'''
for i in range(row):
    list1 = []
    for j in range(column):
        list1.append(int(input()))
    mat1.append(list1)

'''Taking input for second matrix'''
row1 = int(input("Please enter the no of rows for 2nd matrix"))
column1 = int(input("Please enter the number of columns for 2nd matrix"))
print("Pleas enter the values of second matrix here")
for k in range(row1):
    list1 = []
    for l in range(column1):
        list1.append(int(input()))
    mat2.append(list1)
    
    #print(mat1)
    #print(mat2)
    
'''converting both the matrix to numpy arrary for easy manipulation of matrix'''
mat_arr1=np.asarray(mat1)
mat_arr2=np.asarray(mat2)

print(mat_arr1)
print(mat_arr2)
'''Performing matrix manipulation methods here which are inbuilt provided by numpy'''

print ("Addition of two matrices: ")
print (np.add(mat_arr1,mat_arr2))

print ("Subtraction of two matrices : ")
print (np.subtract(mat_arr1,mat_arr2))

print ("Multiplication of two matrices: ")
print (np.multiply(mat_arr1,mat_arr2))

print ("Matrix transposition : ")
print (mat_arr1.T)

print ("Determinant of a matrix: ")
det1 = np.linalg.det(mat_arr1)
print(det1)

print ("Inverse of a matrix: ")
inv1 = np.linalg.inv(mat_arr1)
print(inv1)

print ("Adjoint of a matrix: ")
adj1 = np.matrix.getH(mat_arr1)
print(adj1)


    
    
    

