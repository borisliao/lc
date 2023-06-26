# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        while True:
            num1+=str(l1.val)
            if(l1.next == None):
                break
            l1 = l1.next

        while True:
            num2+=str(l2.val)
            if(l2.next == None):
                break
            l2 = l2.next

        calc = int(num1) + int(num2)
        
        if len(str(calc)) == 1:
            return ListNode(val=int(calc))

        def f(ln, v) :
            print(ln.val)
            print(v)
            ln.val = int(v)
            if(len(v) == 1):
                return
            ln.next = ListNode()
            f(ln.next, v[1:])
        
        result = ListNode()
        f(result,str(calc)[::-1])

        return result
x = Solution()
l1 = ListNode(val=2,next=ListNode(val=4,next=ListNode(val=3)))
l2 = ListNode(val=5,next=ListNode(val=6,next=ListNode(val=4)))
while True:
    result = x.addTwoNumbers(l1,l2)
    print(result.val)
    if(result.next == None):
        break
    result = result.next