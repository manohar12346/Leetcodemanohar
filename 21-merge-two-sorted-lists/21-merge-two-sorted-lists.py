# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
                
        z=ListNode()
        g=z
        while(l1 and l2):
            if l1.val<l2.val:
                z.next=l1
                l1=l1.next
            else:
                z.next=l2
                l2=l2.next
            z=z.next
        if l1:
            z.next=l1
        if l2:
            z.next=l2
        return g.next