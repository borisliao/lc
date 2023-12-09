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

def two_pointers(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Hint from Neetcode
    https://www.youtube.com/watch?v=XVuQxVej6y8
    """
    dummy = ListNode(val=None, next=head)
    l, r = dummy, head

    while n:  # note: we are guaranteed that r.next will exist with `1 <= n <= sz` constraint
        r = r.next  # [2,3,4,5], [3,4,5]
        n -= 1  # 1, 0

    # if n:  # note: we are guaranteed that n = 0 with `1 <= n <= sz` constraint
    #     return head

    while r:  # [3,4,5]
        r = r.next
        l = l.next

    l.next = l.next.next

    return dummy.next


def review1(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Anki 12-8-23
    Used: Solution (3), debugger (4)
    Time: 26:40
    """
    dummy = ListNode(val=None, next=head)  # s6
    node = head
    nth = dummy  # d4, #s7
    for _ in range(n):  # d2, d3, d5
        node = node.next

    while node:
        nth = nth.next
        node = node.next

    nth.next = nth.next.next

    return dummy.next  # s6
