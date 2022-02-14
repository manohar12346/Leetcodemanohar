# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
       
       
        if root:
            ans=[]
            def inord(root):
                if root==None:
                    return 

                ans.append(root.val)
                inord(root.left)
                inord(root.right)
            inord(root)

            root.left=None
            root.right=None
            h=root
            for i in ans[1:]:
                new=TreeNode(i)
                root.right=new
                root.left=None
                root=root.right



            return h.right
        return []
        