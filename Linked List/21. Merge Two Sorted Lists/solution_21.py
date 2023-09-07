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


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    p = res

    while list1 and list2:
        if list1.val > list2.val:
            p.next = list2
            list2 = list2.next

            p = p.next
        else:
            p.next = list1
            list1 = list1.next

            p = p.next

    if list1:
        p.next = list1
    else:
        p.next = list2

    return res.next
