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


def review1(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Anki 12-10-23
    Used: debugger (1)
    Time: 22:25
    """
    result = ListNode()
    node = result
    while list1 or list2:  # d1
        if list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
                node = node.next
            else:
                node.next = list1
                list1 = list1.next
                node = node.next
        elif list1:
            node.next = list1
            break
        else:
            node.next = list2
            break

    return result.next


def review2(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Anki 12-10-23
    Used: debugger 3, solution 1
    Time: 16:17
    """
    dummy = ListNode()  # s1
    head = dummy  # d4

    while list1 or list2:
        if list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2  # d3
                list2 = list2.next
            else:
                dummy.next = list1  # d3
                list1 = list1.next
            dummy = dummy.next
        elif list1:
            dummy.next = list1
            break  # d2
        else:
            dummy.next = list2
            break  # d2

    return head.next  # d4
