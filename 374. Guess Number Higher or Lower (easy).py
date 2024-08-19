#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def guessNumber(self, n: int) -> int:
        upper = 2**32 - 1
        lower = 1
        while guess(n):
            if guess(n) > 0:
                lower = n
            else:
                upper = n
            n = (lower + upper) // 2
        return n

