# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        l=head
        j=head
        while(j and j.next):
            l=l.next
            j=j.next.next
            if l==j:
                return True
        return False