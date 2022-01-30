# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            b=0
            new=ListNode()
            d=new
            
            while(l1 and l2):
                su=l1.val+l2.val+b
                if su>9:
                    b=int(str(su)[0])
                    ne=ListNode()
                    ne.val=int(str(su)[1])
                    new.next=ne
                    new=ne
                else:
                    ne=ListNode()
                    ne.val=su
                    new.next=ne
                    new=ne
                    b=0
                l1=l1.next
                l2=l2.next
            
            if (l1):
                print(l1.val)
                while(l1):
                    ne=ListNode()
                    su=l1.val+b
                    if su>9:
                        b=int(str(su)[0])
                        ne.val=int(str(su)[1])
                        new.next=ne
                        new=ne
                    else:
                        ne.val=su
                        new.next=ne
                        new=ne
                        b=0
                    l1=l1.next
            else:
                if (l2):
                    while(l2):
                        ne=ListNode()

                        su=l2.val+b
                        if su>9:
                            b=int(str(su)[0])
                            ne.val=int(str(su)[1])
                            new.next=ne
                            new=ne
                        else:
                            ne.val=su
                            new.next=ne
                            new=ne
                            b=0
                        l2=l2.next
            print(b)
            if b>0:
                ne=ListNode()
                ne.val=b
                new.next=ne
               
                
                    
                    
            return d.next
                    
                    
                    
                    
                            
                
            
                        
            
                    

            
            
            
        
        