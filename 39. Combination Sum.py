#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(combo):
            nonlocal target, results
            if combo:
                currSum = sum(combo)
            else:
                currSum = 0
            for candidate in candidates:
                if currSum + candidate == target:
                    to_add = sorted(combo + [candidate])
                    if to_add not in results:
                        results.append(to_add)
                elif currSum + candidate > target:
                    pass
                else:
                    to_call = combo + [candidate]
                    dfs(to_call)
                
        
        dfs([])
        
        return results

