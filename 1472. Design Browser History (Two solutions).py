#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = homepage
        self.visitedPages = [homepage]
        self.currentPage = 0

    def visit(self, url: str) -> None:
        self.visitedPages = self.visitedPages[0:self.currentPage+1]
        self.visitedPages.append(url)
        self.currentPage += 1

    def back(self, steps: int) -> str:
        self.currentPage = max(0,self.currentPage - steps)
        return self.visitedPages[self.currentPage]

    def forward(self, steps: int) -> str:
        self.currentPage = min(len(self.visitedPages) - 1,self.currentPage + steps)
        return self.visitedPages[self.currentPage]


"""
class Page:
    def __init__(self,url,prev_page = None, next_page = None):
        self.url = url
        self.prev = prev_page
        self.next = next_page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.currentPage = self.homepage

    def visit(self, url: str) -> None:
        self.currentPage.next = Page(url,prev_page = self.currentPage)
        self.currentPage = self.currentPage.next

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.currentPage.prev:
                self.currentPage = self.currentPage.prev
            steps -= 1
        return self.currentPage.url

    def forward(self, steps: int) -> str:
        while steps>0:
            if self.currentPage.next:
                self.currentPage = self.currentPage.next
            steps -= 1
        return self.currentPage.url
"""

