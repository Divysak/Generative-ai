#211 Basic array using list
arr=[1,2,3]; print(arr)
#212 Access
print(arr[1])
#213 Modify
arr[1]=99; print(arr)
#214 Append
arr.append(4); print(arr)
#215 Remove
arr.remove(99); print(arr)

#216 Numpy import
import numpy as np
#217 Create numpy array
a=np.array([1,2,3]); print(a)
#218 Shape
print(a.shape)
#219 Zeros
print(np.zeros(5))
#220 Ones
print(np.ones(5))

#221 Arrange
print(np.arange(1,6))
#222 Reshape
b=np.arange(6).reshape(2,3); print(b)
#223 Slice
print(b[:,1])
#224 Add arrays
print(a + np.array([4,5,6]))
#225 Multiply
print(a * 2)

#226 dot product
x=np.array([1,2]); y=np.array([3,4])
print(np.dot(x,y))
#227 Max Min
print(np.max(a), np.min(a))
#228 Mean
print(np.mean(a))
#229 Sum
print(np.sum(a))
#230 Transpose
print(b.T)

#231 Indexing
print(b[1,2])
#232 Boolean indexing
print(a[a>1])
#233 Random array
print(np.random.randint(1,10,5))
#234 Unique
print(np.unique([1,2,1,3]))
#235 Flatten
print(b.flatten())

#236 Stack arrays
c=np.array([7,8,9])
print(np.vstack([a,c]))
#237 Split arrays
print(np.split(a,3))
#238 Round
print(np.round([2.333,5.678],2))
#239 Argsort
print(np.argsort([4,1,3]))
#240 Sqrt
print(np.sqrt([4,9,16]))
