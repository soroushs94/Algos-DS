#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 1
        self.res = None

        def inOrder(root):
            #nonlocal count, res
            if not root:
                return
            
            if self.count <= k:
                inOrder(root.left)
                if self.count == k:
                    self.res = root.val
                    self.count += 1
                else:
                    self.count += 1
                inOrder(root.right)

        inOrder(root)
        return self.res


        

