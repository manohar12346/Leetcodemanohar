# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def ke(root):
            if root==None:
                return
            ke(root.left)
            ans.append(root.val)
            ke(root.right)
        ke(root)
        return ans[k-1]
    