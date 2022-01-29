# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        x=head
        while(x!=None):
            c=c+1
            x=x.next
        
        ans=c//2+1
        a=0
        x=head
        while(a!=ans-1):
            x=x.next
            a=a+1
        return x
            
            
            
        
        