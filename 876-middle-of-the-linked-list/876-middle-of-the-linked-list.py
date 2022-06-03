# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        d=head
        while(d and d.next):
            c=c.next
            d=d.next.next
        return c
    
            
            
            
        
        