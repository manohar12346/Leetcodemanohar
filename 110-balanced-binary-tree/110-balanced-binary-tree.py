# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            ct=[0]
            cm=[0]
            def left(rt,c):
                if rt==None:
                    if c>ct[0]:
                        ct[0]=c
                    return
                left(rt.left,c+1)
                left(rt.right,c+1)
            
            def ri(rt,c):
                if rt==None:
                    if c>cm[0]:
                        cm[0]=c
                    return
                ri(rt.left,c+1)
                ri(rt.right,c+1)
       

            que=[root]
            
            while(len(que)>0):
                ct[0]=0
                cm[0]=0
                left(que[0].left,0)
                ri(que[0].right,0)
               
                print(cm[0],ct[0])
                if abs(cm[0]-ct[0])>1:
                    return False
                if que[0].left:
                    que.append(que[0].left)
                if que[0].right:
                    que.append(que[0].right)
                que.remove(que[0])
                
                
            
            return True
        return True
        