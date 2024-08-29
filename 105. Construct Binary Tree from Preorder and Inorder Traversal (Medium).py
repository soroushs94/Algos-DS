#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(val = preorder[0])
        idx = inorder.index(preorder[0])
        if idx > 0:
            l_inorder = inorder[0:idx]
            l_preorder = preorder[1:idx+1]
            root.left = self.buildTree(l_preorder, l_inorder)
        if idx < len(preorder) - 1:
            r_preorder = preorder[idx+1:]
            r_inorder = inorder[idx+1:]
            root.right = self.buildTree(r_preorder, r_inorder)

        return root


# In[ ]:




