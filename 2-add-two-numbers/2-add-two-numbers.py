# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            s=0
            ans=ListNode()
            head=ans
            c=0
            su=l1
            u=l2
            while(su.next or u.next):
                new=ListNode(c,None)
                ans.next=new
                ans=new
                if su.next:
                    su=su.next
                if u.next:
                    u=u.next
                c=c+1
            so=0
            
            
                
            an=head
            va=-1
            
            while(head):
                if l1 and l2:
                    
                    va=l1.val+l2.val+s
                    if va>9:
                        d=int(str(va)[1])
                        s=int(str(va)[0])
                        head.val=d
                        


                    else:
                        s=0
                        head.val=va
                    l1=l1.next
                    l2=l2.next
                    head=head.next
                elif l1:
                    while(head and l1):
                        va=l1.val+s
                        if va>9:
                            d=int(str(va)[1])
                            s=int(str(va)[0])
                            head.val=d
                        else:
                            s=0
                            head.val=va
                        head=head.next
                        l1=l1.next
                elif l2:
                    while(head and l2):
                        va=l2.val+s
                        if va>9:
                            d=int(str(va)[1])
                            s=int(str(va)[0])
                            head.val=d
                        else:
                            s=0
                            head.val=va
                            
                        l2=l2.next
                        head=head.next
               
                else:
                    break
            if va>9:
                f=int(str(va)[0])
                last=ListNode(f,None)
                head=an
                while(head.next):
                    head=head.next
                head.next=last

                
            return an
                    
                            
                
            
                        
            
                    

            
            
            
        
        