# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=ListNode()
        l.next=head
        p1=l
        p2=l
        c=0
        if p1.next.next==None:
            return None
        while(p1.next):
            c=c+1
            if c>n:
                p1=p1.next
                p2=p2.next
            else:
                p1=p1.next
            
            
        if p2==l:
            return l.next.next
        d=p2.next
        p2.next=d.next
        return head
            
            
        
        