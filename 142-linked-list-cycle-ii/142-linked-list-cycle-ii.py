# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        g=head
        h=head
        while(g and g.next):
            
            x.append(g)
            g=g.next
            if g in x:
                return g
        return None
        
            
        