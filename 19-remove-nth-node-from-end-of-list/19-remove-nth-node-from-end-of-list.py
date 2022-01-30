# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=1
        s=head
        while(s.next!=None):
            s=s.next
            x=x+1
        ans=x-n
        
        
        if ans==0:
            head=head.next
            return head
            
        
        else:
            
            
            x=0
            s=head
            while(x!=ans-1):
                x=x+1
                s=s.next
            d=s.next
            s.next=d.next
            return head
        
            
            
        
        