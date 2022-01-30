# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=ListNode()
        b=a
        while(l1 and l2):
            if l1.val>l2.val:
                a.next=l2
                l2=l2.next
            else:
                a.next=l1
                l1=l1.next
            a=a.next
        if l1==None:
            a.next=l2
        else:
            a.next=l1
        return b.next
            
            
                
        