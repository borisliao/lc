from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
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


# def initialAttempt(head: Optional[ListNode]) -> None:
#     """
#     Do not return anything, modify head in-place instead.
#     Does not work
#     """
#     h = []

#     p = head
#     count = 0
#     while p:
#         if count % 2 == 0:
#             h.append(p)
#         count += 1

#         p = p.next

#     p = head
#     count = 0
#     while h:
#         if count % 2 == 1:
#             val = h.pop(0)
#             val.next = p
#         count += 1

#         p = p.next

def attempt1(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    Done with NeetCode guide: https://www.youtube.com/watch?v=S5bfdUTrKLM
    """
    # -----find middle-----
    # [1, 2, 3, 4, 5]
    if head.next == None:
        return
    # slow, fast pointers
    slow, fast = head, head.next  # [1, 2, 3, 4, 5] [2, 3, 4, 5]

    while fast and fast.next:
        slow = slow.next  # [2, 3, 4, 5],
        fast = fast.next.next  # [3, 4, 5],

    # -----reverse second half-----
    # same to leetcode problem:
    # Linked List\206. Reverse Linked List
    # https://leetcode.com/problems/reverse-linked-list/+

    # start of second half
    # [1, 2, 3] [4, 5]
    l2 = slow.next
    # break the link between list 1 and list 2
    slow.next = None

    prev, curr = None, l2

    while curr:
        curr_next = curr.next
        curr.next = prev

        prev = curr
        curr = curr_next

    l2 = prev

    # -----merge two halfs-----
    # [1, 2, 3] [5, 4]
    l1 = head

    while l2:
        l1_next = l1.next  # [2, 3], [3]
        l2_next = l2.next  # [4], None

        l1.next = l2  # [1, 5, 4], [3, 4]
        l2.next = l1_next  # [1, 5, 2, 3], [None]

        l1 = l1_next  # [2, 3], [3]
        l2 = l2_next  # [4], None


def neetcode(head: ListNode) -> None:
    """
    https://www.youtube.com/watch?v=S5bfdUTrKLM
    """
    # find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# def review1(head: ListNode) -> None:
#     """
#     Anki 12-13-23
#     """
#     even: list[ListNode] = []
#     odds: list[ListNode] = []

#     i = 0
#     while head:
#         state = 'odd' if i % 2 == 1 else 'even'
#         if state == 'odd':
#             odds.append(head)
#         else:
#             even.append(head)
#         head = head.next
#         i += 1

#     i = 0
#     while odds or even:
#         if even[0]:
#             even[0].next


def review2(head: ListNode) -> None:
    """
    Anki 12-14-23
    """
    # find midpoint
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second half
    second_half = slow.next

    slow.next = None
    node = second_half
    prev_node = None
    while node:
        temp_node = node.next
        node.next = prev_node
        prev_node = node
        node = temp_node

    # merge lists
    first_half = head
    second_half = prev_node  # s3

    while second_half:  # s2 was first_half
        temp1, temp2 = first_half.next, second_half.next  # s1
        first_half.next = second_half  # s1
        second_half.next = temp1  # s1

        first_half, second_half = temp1, temp2  # s1

    return head
