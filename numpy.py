import numpy as np

a = np.array([1,2,3])
print('Array a',a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print('Array b',b)

#   Get Dimension
print('Dimension\n','a',a.ndim,'b',b.ndim)

#   Get Shape
print('Shape\n','a',a.shape,'b',b.shape)

#   Get data Type
print('Data type\n','a',a.dtype,'b',b.dtype)

c = np.array([1,2,3], dtype='int16')

#   Get size of memory used (bytes)
print('Size of memory used\n','a',a.itemsize,'c',c.itemsize)

#   Get numer of elements
print('Number of elements\n','a',a.size,'b',b.size)

#   Get total size in bytes
print('Total Size\n','a',a.size * a.itemsize,'b',b.size * b.itemsize)
print('Total Size\n','a',a.nbytes,'b',b.nbytes)

#################################

#   Accessing/Changing specific element, rows, columns, etc.
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('a',a)

#   Get specific element [row, column]
print('Get element\n2-6:',a[1,  5])
print('Get element\n2-6:',a[1, -2])

#  Get specific row
print('Get row\n1:',a[0, :])

#   Get specific column
print('Get column\n3:',a[:, 2])

#   Get specific values [startindex:endindex:stepsize]
print('''Get specific elements
Row: 1, form col 2, end col 7, every second value:''',a[0, 1:6:2])
print('''Get specific elements
Row: 1, form col 2, end col 7, every second value:''',a[0, 1:-1:2])

#   Changing value
a[1,5] = 20
print('After change 1 value\na:',a)

#   Changing all values in column
a[:, 2] = 5
print('After change 1 column with one new value\na:',a)
a[:, 2] = [1,2]
print('After change 1 column with set of values \na:',a)

#   3-d array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print('3-d array\nb:',b)

#   Get value of 3-d array
print('Get value of 3-d array\n1-2-2:',b[0,1,1])

#   Replace set of values in 3-d array
b[:,1,:] = [[9,9],[8,8]]
print('After replace\nb:',b)

##################################

#   Initializing Different types od Arrays

#   All 0s matrix
a = np.zeros(5)
print('Array of \'Zeros\'\na:',a)
a = np.zeros((2,3))
print('Array of \'Zeros\'\na:',a)
a = np.zeros((2,3,4))
print('Array of \'Zeros\'\na:',a)

#   All 1s matrix
a = np.ones(5)
print('Array of \'Ones\'\na:',a)
a = np.ones((2,3))
print('Array of \'Ones\'\na:',a)
a = np.ones((2,3,4), dtype='int16')
print('Array of \'Ones\'\na:',a)

#   Any other number
a = np.full((2,2), 99)
print('Array of \'99\'\na:',a)

#   Any other number (full_like)
b = np.full_like(a, 7)
print('Array full_like with \'7\'\nb: ',b)

#   Random decimal numbers
c = np.random.rand(4,2)
print('Array with random values\nc:',c)

#   Random decimal numbers
c = np.random.randint(2,7, size=(3,3))
print('Array with random values\nc:',c)

#   Identity matrix
print('Identity matrix\n',np.identity(5,dtype='int8'))

#   Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print('Repeted array\n',r1)

#   Copy arrays
a = np.array([1,2,3])
b = a.copy()
b[0]=100
print('Copy array\na:',a,'b:',b)

#####################
#   Mathematics

a = np.array([1,2,3,4])
print('a:',a)

print('a + 2',a+2)
print('a - 2',a-2)
print('a * 2',a*2)
print('a / 2',a/2)
print('a ** 2',a ** 2)
print('sin(a)',np.sin(a))

b = np.array([1,0,1,0])
print('b:',b,'\na+b:',a+b)

#####################
#   Linear Algebra

a = np.ones((2,3))
b = np.full((3,2), 2)

print('a:',a,'\nb:',b)

print('matmul a*b\n',np.matmul(a,b))

c = np.identity(3)
print('c:\n',c,'\nnp.linalg.det(c):\n',np.linalg.det(c))
