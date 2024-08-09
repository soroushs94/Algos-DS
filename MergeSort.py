#!/usr/bin/env python
# coding: utf-8

# In[ ]:


array = [5,4,2,6,4,8,1,4,8,3,0,9]

def mergeSort(arr,s,e):
    
    if e<=s:
        return arr
    
    m = (e+s) // 2
    
    mergeSort(arr,s,m)
    mergeSort(arr,m+1,e)
    merge(arr,s,e)
    
    return arr

def merge(arr,s,e):
    
    m = (s+e)//2
    
    l = arr[s:m+1]
    r = arr[m+1:e+1]
    
    i = 0
    j = 0
    k = s
    
    while (i<m-s+1) and (j<e-m):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
            k += 1
        else:
            arr[k] = r[j]
            j += 1
            k += 1
            
    while i < m-s+1:
        arr[k] = l[i]
        k += 1
        i += 1
        
    while j < e-m:
        arr[k] = r[j]
        k += 1
        j += 1
        
    return arr

mergeSort(array,0,len(array)-1)

