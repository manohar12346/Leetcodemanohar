# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        he=head
        if he== None:
            return None
        d=0
        l=he
        while(l):
            d=d+1
            l=l.next
        k=k%d
        while(k>0):
            
            j=he
            l=j.val
            while(j and j.next):
                ac=l
                l=j.next.val
                j.next.val=ac
                
                
                j=j.next
            he.val=l
            k=k-1
            
        return he