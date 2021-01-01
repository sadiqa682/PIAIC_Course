#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2

# # Create One d array into 2 d array with 2 rows

# In[2]:


import numpy as np
M = np.arange(10)
M_1= M.reshape(2,5)
M_1


# ## How to stack two arrays vertically

# In[8]:


X_1 = np.array([[0,1,2,3],[4,5,6,7]])
X_2= np.array([[9,10,11,12],[9,8,7,6]])
X_n = np.array([[1,1,1,1],[1,1,1,1]])
X_3 = np.vstack((X_1,X_2,X_n))
X_3


# # How to stack two arrays horizontally

# In[10]:


import numpy as np
X_4 = np.array([[0,1,2,3],[1,1,1,1]])
X_5 = np.array([[4,5,6,7],[0,1,0,1]])
X_out = np.hstack((X_4,X_5))
X_out


# ## How to convert an array of arrays into flat one dim array

# In[9]:


arr = np.array([[1,2,3],[4,5,6],[9,7,0]])
arr
arr3= arr.flatten() # first possibility
arr3
result = arr.ravel() # second way
result


# ## How to convert higher dimension into one dimension

# In[13]:


arr4 = np.arange(24)
arr_4 =arr4.reshape(2,4,3)
arr_5 = arr_4.flatten()
arr_5
### Use ravel
arr_6 = arr_4.ravel()
arr_6


# ## Q6  Convert One dimension to higher dimension

# In[14]:


arr7 = np.arange(24)
Arr7= arr7.reshape(3,2,4)
Arr7


# ## Q7 Create 5*5 array and find square of an array

# In[18]:


arr8 = np.arange(25)
Arr8 = arr8.reshape(5,5)
Arr_8= np.square(Arr8)
Arr_8


# ## Q8 Create 5*6 array and find its mean

# In[21]:


arr9=np.arange(30)
Arr9 = arr9.reshape(5,6)
Mean_9= np.mean(Arr9)
Mean_9


# ## Q.9 Find the atandard deviation of the matrix in Q.8

# In[22]:


Standard_dev = np.std(Arr9)
Standard_dev


# ## Q10 Find the median of the array in Q8

# In[23]:


Median8 = np.median(Arr9)
Median8


# ## Q 11 Find transpose of the array in Q8

# In[25]:


Transpose8 = np.transpose(Arr8)
Transpose8


# ## Q12 Create 4*4 array and find the sum of its diagonal elements

# In[44]:


import numpy as np
arr12=np.array([[5,3,4,10],[5,6,3,4],[10,11,12,4],[4,6,9,100]])
ArrT=np.trace(arr12)
ArrT


# ## Q 13 Find the determinant of the previous array in Q 12

# In[53]:


dt_8 = np.linalg.det(arr12)
print("\ndeterminant of a given 4*4 matrix is: ")
#print(int\(det))
#dt_8
print(dt_8)


# ## Q 14 Find the 5th and 95th percentile of an array

# In[57]:


array1=np.array([2,3,4,6,7,8,9,10,23,12,14,15,16,25,20])
print("\narray is :",array1)
print("5th percentile of an array :", np.percentile(array1,5))
print("95th percentile of an array :", np.percentile(array1,95))


# ## Q15 How to find if a given array has any null value

# In[66]:


array15 = np.array([1,2,3,4,5,6, 0, 8,9,10,11,12,13,1,4,15,21])
array_nan=np.isnan(array15)
print(array_nan)


# In[ ]:




