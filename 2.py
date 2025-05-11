class ListNode:
    def __init__(self,val=0,next=None):
      self.val=val
      self.next=next
def build_link_list(numbers):
    d=ListNode()
    current=d
    for n in numbers:
        current.next=ListNode(n)
        current=current.next
    return d.next
def printList(n):
    l=[]
    while n:
        l.append(n.val)
        n=n.next
    print(l)
        
class Solution():
    def add2numbers(self,l1,l2):
        dummy=ListNode()
        carry=0
        current=dummy
        while l1 or l2 or carry:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            total=v1+v2+carry
            carry=total//10
            digit=total%10
            current.next=ListNode(digit)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
                
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=build_link_list(l1)
l2=build_link_list(l2)
s=Solution()
r=s.add2numbers(l1,l2)
printList(r)
