# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            que=[[root,1]]
            ma=1

            while(len(que)>0):
                x=que[0][1]
                if x>ma:
                    ma=x
                if que[0][0].left:
                    que.append([que[0][0].left,x+1])
                if que[0][0].right:
                    que.append([que[0][0].right,x+1])
                que.remove(que[0])
            return ma
        return 0

