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
    if head.next == None: return
    # slow, fast pointers
    slow, fast = head, head.next # [1, 2, 3, 4, 5] [2, 3, 4, 5]

    while fast and fast.next: 
        slow = slow.next # [2, 3, 4, 5],
        fast = fast.next.next # [3, 4, 5], 
    
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
        l1_next = l1.next # [2, 3], [3]
        l2_next = l2.next # [4], None

        l1.next = l2 # [1, 5, 4], [3, 4]
        l2.next = l1_next # [1, 5, 2, 3], [None]

        l1 = l1_next # [2, 3], [3]
        l2 = l2_next # [4], None
    