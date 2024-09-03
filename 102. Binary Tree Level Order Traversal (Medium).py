#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            lev_res = []
            for i in range(len(queue)):
                item = queue[0]
                queue.remove(item)
                lev_res.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            res.append(lev_res)

        return res


# In[ ]:


from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            lev_res = []
            for i in range(len(queue)):
                item = queue.popleft()
                lev_res.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            res.append(lev_res)

        return res

