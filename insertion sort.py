#!/usr/bin/env python
# coding: utf-8

# In[8]:


arr = [5,4,6,8,1,12,3,2,1]

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                swap(arr,j,j+1)
insertionSort(arr)
arr

