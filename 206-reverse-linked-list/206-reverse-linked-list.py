# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need three varibles one for traversion in front(p) and one for current varibale(q) and last one for previous variable(r) so the present (q) adress should br changed to last one adress (r) at one hand we need to move p otherwise as we are changing the adreess the loop we will not move
        
        
        prev=None
    
        pre=None
        nex=head
        while(nex):
            prev=pre
            pre=nex
            nex=nex.next
            pre.next=prev
        head=pre
        return head
    
        
            
        