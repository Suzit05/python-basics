#py 04-numpy.py
import numpy as np 
arr=np.array([1,2,4])

print(arr*2)

#1.Creating 1d array

arr1=np.array([10,20,30,40])
print("\n 1D ARRAY: \n", arr1)

#2.Create 2d array
arr2=np.array([[2,4,5],[6,9,7]])
print("\n 2d array: \n:", arr2)

#3.reshape array used to change the subject of the array without changing its data

reshaped=arr2.reshape(3,2) #3r 2c
print("\n 2d reshaped array: \n:", reshaped)

print("sum:", arr1.sum())
print("mean:", arr1.mean())
print("max:",arr1.max())
print("min:",arr1.min())
print("sum:",arr2.sum())
print("mean:",arr2.mean())