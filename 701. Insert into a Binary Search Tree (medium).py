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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root

        """
        if root.val > val:
            if root.left:
                if self.getMax(root.left) < val:
                    root.left = TreeNode(val,left = root.left)
                else:
                    root.left = self.insertIntoBST(root.left,val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                if self.getMin(root.right) > val:
                    root.right = TreeNode(val, right = root.right)
                else:
                    root.right = self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val)
        return root


    def getMin(self,root):
        minNode = root
        while minNode.left:
            minNode = minNode.left
        return minNode.val
    
    def getMax(self,root):
        maxNode = root
        while maxNode.right:
            maxNode = maxNode.right
        return maxNode.val                                          
    """
        


# In[ ]:




