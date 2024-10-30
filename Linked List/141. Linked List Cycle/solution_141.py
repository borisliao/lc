class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next
        self._nodes = set()

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: 'list'):
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


def review1(head: ListNode | None) -> bool:
    """
    Anki 12-12-23
    Used: Debugger (1)
    Time: 18:30
    """
    slow = head
    fast = head

    while slow and fast:
        if slow:
            slow = slow.next

        for _ in range(2):
            if fast:
                fast = fast.next

        if slow == fast and slow != None:  # d1 slow != None for single node case
            return True

    return False


def review2(head: ListNode | None) -> bool:
    """
    Anki 12-18-23
    Time: 4:07
    """
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False


def review3(head: ListNode | None) -> bool:
    """
    Anki 1-7-24
    Time: 2:30
    """
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


def review4(head: ListNode) -> bool:
    """
    Mochi 4-16-24
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def review5(head: ListNode) -> bool:
    """
    Mochi 10-29-24
    """
    slow, fast = head, head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
