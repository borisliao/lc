class ListNode:
    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: list):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __repr__(self):
        return f"({self.val}, {self.next})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


def two_pointers(head: ListNode | None, n: int) -> ListNode | None:
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


def review1(head: ListNode | None, n: int) -> ListNode | None:
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


def review2(head: ListNode | None, n: int) -> ListNode | None:
    """
    Anki 12-9-23
    Time: 3 min
    """
    dummy_node = ListNode(val=None, next=head)
    l = dummy_node
    r = head

    for _ in range(n):
        r = r.next

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next

    return dummy_node.next


def review3(head: ListNode | None, n: int) -> ListNode | None:
    """
    Anki 12-24-23
    Time: 12 min
    Used: Debugger 1
    """
    dummy = ListNode(next=head)
    l = dummy
    r = dummy

    for _ in range(n+1):
        r = r.next

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next

    return dummy.next  # d1 head


def review4(head: ListNode | None, n: int) -> ListNode | None:
    """
    Anki 1-19-24
    Time: 10 min
    """
    dummy = ListNode()
    dummy.next = head
    fast, slow = dummy, dummy

    while n:
        fast = fast.next
        n -= 1

    fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


def review5(head: ListNode | None, n: int) -> ListNode | None:
    """
    Mochi 4-19-24
    """
    dummy = ListNode(0, next=head)
    slow, fast = dummy, head

    for _ in range(n):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next  # d1 head


def review6(head: ListNode | None, n: int) -> ListNode | None:
    """
    Mochi 10-30-24
    """
    dummy = ListNode(0, next=head)
    fast = head
    slow = dummy
    for _ in range(n):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
