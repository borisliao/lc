from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self._nodes = set()

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: List):
            list.append(ln.val)
            self._nodes.add(self)

            # TODO: fix bug where last node of cyclical list does not get represnted
            if (ln.next and ln.next not in self._nodes):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __repr__(self):
        return f"({self.val}, {self.next})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)

    def __hash__(self):
        return id(self)


def hashSet(head: Optional[ListNode]) -> bool:
    """Naive solution, Space complexity O(n)"""
    nodes = set()

    while head:
        if head in nodes:
            return True

        nodes.add(head)

        head = head.next

    return False


def floyds(head: Optional[ListNode]) -> bool:
    """
    Hint from neetcode https://www.youtube.com/watch?v=gBTe7lFR3vc
    Floyd's Tortoise and Hare algorithm guarantees a solution
    """
    f, s = head, head

    while f and f.next:
        # start the race!
        s = s.next
        f = f.next.next

        # check status of race
        if f == s:
            return True

    return False
