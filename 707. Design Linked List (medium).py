#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val,prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        i = 0
        node = self.head
        while node:
            if i == index:
                return node.val
            i += 1
            node = node.next
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            node = ListNode(val,next = self.head)
            self.head.prev = node
            self.head = node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val,prev=self.tail)
            self.tail = self.tail.next
        
    def addAtIndex(self, index: int, val: int) -> None:
        if (not self.head) and index != 0:
            return 
        elif index ==0:
            self.addAtHead(val)
            return
        else:
            i = 0
            curr_node = self.head
            while curr_node:
                if i == index:
                    node = ListNode(val,next=curr_node,prev=curr_node.prev)
                    curr_node.prev.next = node
                    curr_node.prev = node
                    return
                i+=1
                curr_node = curr_node.next
            if i == index:
                self.addAtTail(val)
            return

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index==0:
            if not self.head.next:
                self.head = None
                self.tail = None
                return
            self.head = self.head.next
            self.head.prev = None
        else:
            curr_node = self.head
            i = 0
            while curr_node:
                if i == index:
                    if curr_node == self.tail:
                        self.tail = self.tail.prev
                    else:
                        curr_node.next.prev = curr_node.prev
                    curr_node.prev.next = curr_node.next
                    
                    return
                i += 1
                curr_node = curr_node.next
            return


# In[ ]:




