#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        if (r ==1) or (self.countHours(piles,1) <=h):
            return 1

        if h == len(piles):
            return r

        while l <= r:
            k = (l+r) // 2
            if (self.countHours(piles, k) <= h):
                if (self.countHours(piles, k-1) > h):
                    return k
                else:
                    r = k 
            else:
                l = k + 1


    
    def countHours(self,piles,k):
        return sum(x//k  if x % k == 0 else x//k + 1 for x in piles)

