# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            ans=[]
            for i in range(1000):
                ans.append([])
            
            
            que=[[root,0]]
            while(len(que)>0):
                x=que[0]
                
                ans[x[1]].append(x[0].val)
                if x[0].left:
                    
                    que.append([x[0].left,x[1]+1])
                if x[0].right:
                    
                    que.append([x[0].right,x[1]+1])
                

                que.remove(que[0])
            real=[]
           
            for i in ans:
                if i==[]:
                    break
                real.append(i)
            return real
        
            
        return []
        