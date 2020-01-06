import numpy as np
np.array([1,2,3,4,5])


#Generate an array of 5 elements
np.arange(5)
#Generate an array with step size of 2 between 1 to 10.
np.arange(start=1,stop=10,step=2)           #np.arange(1,10,2) 


np.zeros(5)  #Array of Zeros
np.ones(5)   #Array of Onces
np.eye(5)    #Identity Matrix


np.array([[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]]) 


# Create single dimensional array
arr = np.arange(9)
# Use reshape method on single dimensional array to create multidimensional array
mularr = arr.reshape(3,3)
#Chaning can be used to perform in above task in single line
np.arange(9).reshape(3,3)   


#generate single number using rand
np.random.rand()
#generate single dimentional array using rand
np.random.rand(5)
#generate multi dimentional array using rand
np.random.rand(3,3)


#generate single number using randn
np.random.randn()
#generate single dimentional array using randn
np.random.randn(5)
#generate multi dimentional array using randn
np.random.randn(3,3)


#generate single number using randint from 0 to 5 (o inclusive and 5 exclusive)
np.random.randint(5)
#generate single dimentional array using randint with 3 element btw 1 to 5
np.random.randint(1,5,3)
#generate 3 X 3 two dimentional array using randint 
np.random.randint(1,5,[3,3])


#Create array of 4 eqally spaced elements between 1 and 2 both inclusive.
#1st elements is 1 and other elements are spaced with step size of (start-stop)/(num-1)
np.linspace(start=1,stop=2,num=4)         #np.linspace(1,2,4)
#Create array of 4 equally space elements between 1 and 2 excluding 2
#1st elements is 1 and other elements are spaced with step size of (start-stop)/(num)
np.linspace(1,2,4,endpoint=False)
#Print step size in above 2 scenario
np.linspace(start=1,stop=2,num=4,retstep=True)
np.linspace(1,2,4,endpoint=False,retstep=True)


#Array of 10 elements.
arr=np.array([10,20,30,40,50,60,70,80,90,100])
#Select element at 5th index.(indexing starts at 0)
arr[5]
#Select element from 4th index(50) to 8th index(90). Element corresponding to Stop index is not included in sliced array, hence 9th index has been mentioned as Stop index.
arr[4:9]
#Select elemet with a step size of 2  between 0th index and 6th index.
arr[0:6:2]


#Two dimensional array of 5 X 5
mularr=np.arange(25).reshape(5,5)
# Select row-1 to row-5 (exclude row0)
mularr[1:]
#Select col-1 to col-5 (exclude col0)
mularr[:,1:]
#Select everything excluding row-0 and col-0
mularr[1:,1:]           #Or mularr[1:5,1:5]
#Select everything excluding row-4 and col-4
mularr[0:4,0:4]         #Or mularr[:4,:4]
# select 3 X 3 Matrix from the center of 5 X 5 Matrix.
mularr[1:4,1:4]          
# Create an array with step sixe of 2.
mularr[0:5:2,0:5:2]     #Or mularr[::2,::2]


#Method min can be used to find lowest element in an array
mularr.min()
#Method min can be used to find Highest element in an array
mularr.max()
#shape is a attribute of array which provides dimension of array in tuple.
mularr.shape
#dtype is another attribute which provides datatype of the element in array.
mularr.dtype
