#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return
        res = []
        left = self.inorderTraversal(root.left)
        if left:
            res = res + left
        res.append(root.val)
        right = self.inorderTraversal(root.right)
        if right:
            res = res + right
        return res


# In[ ]:




