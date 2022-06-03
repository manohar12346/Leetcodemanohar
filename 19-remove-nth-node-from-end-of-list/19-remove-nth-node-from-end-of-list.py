# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        h=head
        g=head
        t=head
        while(n):
            h=h.next
            n=n-1
        if h==None:
            return head.next
        while(h and h.next):
            h=h.next
            g=g.next
        g.next=g.next.next
        return t

            
        
        