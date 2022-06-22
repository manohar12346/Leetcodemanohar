# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        c=None
        if len(nums)>0:
            mid=len(nums)//2
            node=TreeNode(nums[mid])
            if c==None:
                c=node
            node.left=self.sortedArrayToBST(nums[0:mid])
            node.right=self.sortedArrayToBST(nums[mid+1::])
            
        else:
            return None
        return c