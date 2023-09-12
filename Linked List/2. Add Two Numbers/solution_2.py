# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: List):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)

# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     num1 = ''
#     num2 = ''
#     while True:
#         num1+=str(l1.val)
#         if(l1.next == None):
#             break
#         l1 = l1.next

#     while True:
#         num2+=str(l2.val)
#         if(l2.next == None):
#             break
#         l2 = l2.next

#     calc = int(num1) + int(num2)

#     if len(str(calc)) == 1:
#         return ListNode(val=int(calc))

#     def f(ln, v) :
#         print(ln.val)
#         print(v)
#         ln.val = int(v)
#         if(len(v) == 1):
#             return
#         ln.next = ListNode()
#         f(ln.next, v[1:])

#     result = ListNode()
#     f(result,str(calc)[::-1])

#     return result


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    head = result
    carry = 0

    while l1 or l2 or carry:
        if l1:
            n1 = l1.val
            l1 = l1.next
        else:
            n1 = 0

        if l2:
            n2 = l2.val
            l2 = l2.next
        else:
            n2 = 0

        if carry:
            c = carry
            carry = 0
        else:
            c = 0

        nodeResult = n1 + n2 + c

        if nodeResult > 9:
            carry = nodeResult // 10
            nodeResult -= 10

        result.next = ListNode(nodeResult, None)
        result = result.next

    return head.next
