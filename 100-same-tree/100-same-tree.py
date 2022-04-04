# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue=[[p,q]]
        if not(p) and not(q):
            return True
        elif not(p) or not(q):
            return False
        while(len(queue)>0):
            s=queue[0]
            if s[0].left and not(s[1].left):
                return False
            if s[0].right and not(s[1].right):
                return False
            if not(s[0].left) and (s[1].left):
                return False
            if not(s[0].right) and (s[1].right):
                return False
            
            if s[0].left and s[1].left:
                queue.append([s[0].left,s[1].left])
            if s[0].right and s[1].right:
                queue.append([s[0].right,s[1].right])
            if s[0].val!=s[1].val:
                return False
            queue.remove(queue[0])
        return True
    
                