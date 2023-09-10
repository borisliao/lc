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

    def __repr__(self):
        return f"({self.val}, {self.next})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


# def two_pass(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     """
#     attempt1, Naive approach, 2 passes
#     fails test case 2 due to flawed nth_from_beginning
#     """
#     original_head = head
#     total = 0

#     while head:
#         total += 1
#         head = head.next

#     nth_from_beginning = total - n

#     head = original_head

#     # traverse to nth-1 element from beginning
#     for _ in range(nth_from_beginning - 1):
#         head = head.next

#     # -----remove the nth element-----
#     if head.next:
#         head.next = head.next.next
#     else:
#         head.next = None
#     return original_head
