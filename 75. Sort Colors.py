#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0:0,1:0,2:0}
        for num in nums:
            colors[num] += 1
        
        index = 0
        for key in [0,1,2]:
            for num in range(colors[key]):
                nums[index] = key
                index+= 1 


# In[ ]:




