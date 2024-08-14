#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix,target)
        if row == -1:
            return False
        else:
            return self.binarySearch(matrix[row],target)

    def findRow(self,matrix,target):
        if (matrix[0][0] > target) or (matrix[-1][-1]<target):
            return -1

        l = 0
        r = len(matrix) - 1
        while l <=r:
            m = (l + r) // 2
            if (matrix[m][0]<=target) and (matrix[m][-1]>=target):
                return m
            elif matrix[m][0]>target:
                r = m - 1
            else:
                l = m + 1
        return -1

    def binarySearch(self,arr,target):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (r+l) // 2
            if arr[m] == target:
                return True
            elif arr[m]>target:
                r = m - 1
            else:
                l = m + 1

        return False

