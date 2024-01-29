import heapq
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

    def __bool__(self):
        return bool(self.val or self.next)


# def mergeKLists(lists: list[ListNode]) -> ListNode | None:
#     h: list[tuple[tuple[int, int], ListNode]] = []
#     t = 0
#     for i in range(len(lists)):
#         node = lists[i]
#         while node:
#             heapq.heappush(h, ((node.val, t), node))
#             node = node.next
#             t -= 1

#     head = ListNode()
#     node = head
#     for n in h:
#         node.next = ListNode(n[1].val)
#         node = node.next

#     return head.next

# def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:

#     def merge(l: ListNode, r: ListNode):
#         if not l and not r:
#             return None
#         if l and r:
#             val = 0
#             next = None
#             if l.val > r.val:
#                 val = r.val
#                 next = merge(l, r.next)
#             else:
#                 val = l.val
#                 next = merge(l.next, r)
#             return ListNode(val, next)
#         elif l:
#             return l
#         else:
#             return r

def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 1-29-24
    Used: [https://www.youtube.com/watch?v=DvnxDGkjMDM](https://www.youtube.com/watch?v=DvnxDGkjMDM)
    """
    def merge(l, r):
        """
        1-29-24
        From https://www.youtube.com/watch?v=DvnxDGkjMDM
        Used in 23. Merge k Sorted Lists
        """
        if not l:
            return r
        if not r:
            return l
        if l.val < r.val:
            l.next = merge(l.next, r)
            return l
        else:
            r.next = merge(l, r.next)
            return r

    if not lists:
        return None

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists)-interval, interval * 2):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]


def review1(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 1-29-24
    Time: 15 min
    """
    def merge(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = merge(l1.next, l2)
            return l1
        else:
            l2.next = merge(l1, l2.next)
            return l2

    if not lists:  # d1
        return None  # d1

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval*2):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]


def review2(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 1-29-24
    Time: 12:40
    """
    def merge(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = merge(l1, l2.next)
            return l2
        else:
            l1.next = merge(l1.next, l2)
            return l1

    if not lists:
        return None

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists)-interval, interval*2):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]


# def review3(lists: list[ListNode | None]) -> ListNode | None:
#     """
#     Anki 1-29-24
#     Time: 12:40
#     """
