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
        if root:
            que=[root]
            h=root
            while(len(que)>0):
                s=[]
                while(len(que)>0):
                    if que[0].left:
                        s.append(que[0].left)
                    if que[0].right:
                        s.append(que[0].right)
                    if len(que)==1:
                        que[0].next=None
                    else:
                        que[0].next=que[1]
                    que.remove(que[0])
               
                que=s
                print(s)
                
            return h
        return None
            
        