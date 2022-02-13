# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a=[0]
        def che(r1,r2):
            
            if not(r1) and not(r2):
                return 
            elif r1 and not(r2):
                        a[0]=1
            elif not(r1) and (r2):
                        a[0]=1
            else:
                if r1.val==r2.val:
                    if (r1.left and not(r2.left)) or (r2.left and not(r1.left)):
                        a[0]=1
                    if (not(r2.right) and (r1.right)) or (not(r1.right) and (r2.right)):
                        a[0]=1
                    else:
                        che(r1.left,r2.left)
                        che(r1.right,r2.right)
                                                

                                                

                else:
                    a[0]=1
        che(p,q)
        if a[0]==1:
            return False
        return True
                    
                