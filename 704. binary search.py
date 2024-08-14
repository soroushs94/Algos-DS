#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0, len(nums)-1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        mid = (l+r) //2    

        while mid > l:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
            mid = (l + r) // 2

        return -1

