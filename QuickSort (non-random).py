#!/usr/bin/env python
# coding: utf-8

# In[ ]:


array = [5,4,9,2,6,4,8,1,4,8,3,0,9]

def get_pivot(arr):
    return arr[0]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = get_pivot(arr)
    temp = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            temp.append(arr[i])
            
    for i in range(len(arr)):
        if arr[i] == pivot:
            temp.append(arr[i])
            
    index = len(temp)
    
    if index == len(arr):
        arr[0:index-1] = quickSort(temp[0:index-1])
        arr[index-1] = pivot
        return arr
    
    for i in range(len(arr)):
        if arr[i]>pivot:
            temp.append(arr[i])
    
    arr = temp
    
    arr[0:index] = quickSort(arr[0:index])
    arr[index:] = quickSort(arr[index:])
    
    return arr
    

quickSort(array)

