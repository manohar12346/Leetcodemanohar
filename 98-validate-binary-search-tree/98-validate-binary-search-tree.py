# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        que=[[root,[-10000000000000000000,100000000000000000000000]]]
        while(len(que)>0):
            x=que[0]
           
            if x[0].val <= x[1][0] or x[0].val>=x[1][1]:
                return False
            if x[0].left:
                que.append([x[0].left,[x[1][0],x[0].val]])
            if x[0].right:
                que.append([x[0].right,[x[0].val,x[1][1]]])
            que.remove(x)
        return True
                                

                
            
            