# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        he=head
        ch=head
        co=0
        while(ch):
            co=co+1
            ch=ch.next
        
        if head==None:
            return None
        a=he.val
        k=k%co
        
        for i in range(k):
            h=he
            h=h.next
            while(h):
                va=h.val
                h.val=a
                a=va
                h=h.next
            
            he.val=a
        return he
                
                
                
        
        