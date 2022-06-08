"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        else:
            que=[root]
            while(len(que))>0:
                s=[]
                while(len(que)>1):
                    que[0].next=que[1]
                    if que[0].left:
                        s.append(que[0].left)
                    if que[0].right:
                        s.append(que[0].right)
                    que.remove(que[0])
                if que[0].left:
                        s.append(que[0].left)
                if que[0].right:
                        s.append(que[0].right) 
                que=s
        return root
            
        