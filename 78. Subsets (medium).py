#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]],[]]

        subres = self.subsets(nums[1:])
        to_add = [x+[nums[0]] for x in subres]
        res = subres + to_add
        return res


# In[ ]:




