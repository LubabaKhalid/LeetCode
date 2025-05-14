# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        stack1=[]
        stack2=[]

        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        head=None
        while stack1 or stack2 or carry:
            if stack1:
                x=stack1.pop()
            else:
                x=0
            if stack2:
                y=stack2.pop()
            else:
                y=0
            d=x+y+carry
            carry=d//10
            d=d%10
            node=ListNode(d)
            node.next=head
            head=node
        return node
        