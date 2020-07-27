# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1=0
        q2=0
        count1=0
        count2=0
        while(l1!=None):
            q1=q1+l1.val*pow(10,count1)
            l1=l1.next
            count1+=1
        while(l2!=None):
            q2=q2+l2.val*pow(10,count2)
            l2=l2.next
            count2+=1
        r=ListNode(val=0,next=None)
        result=r
        q3=q1+q2
        while(q3!=0):
            r.val=q3%10
            if q3//10!=0:
              r2=ListNode(val=0,next=None)
              r.next=r2
              r=r2
            else:
              r=None
            q3=q3//10
        return result
                
            
        
