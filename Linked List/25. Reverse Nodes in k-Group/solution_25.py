class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: "list"):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __repr__(self):
        return f"({self.val}, {self.next})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


def reverseKGroup(head: ListNode | None, k: int) -> ListNode | None:
    def reverse(head: ListNode, k: int):
        new_head, prev = None, head

        while k:
            next_node = prev.next
            prev.next = new_head

            new_head = prev
            prev = next_node
            k -= 1

        return new_head

    cur = head
    kTail = None

    new_head = None

    while cur:
        count = 0
        cur = head

        while count < k and cur:
            cur = cur.next
            count += 1

        if count == k:
            rev_head = reverse(head, k)

            if not new_head:
                new_head = rev_head
            if kTail:
                kTail.next = rev_head
            kTail = head
            head = cur
    if kTail:
        kTail.next = head

    return new_head if new_head else head


def review2(head: ListNode | None, k: int) -> ListNode | None:
    """
    Anki 2-4-24
    Used: Solution
    Time: 20 min
    """
    def reverse(head, k):
        """
        head = 3
        next = 3
        prev = 2
        k = 1
        1 -> 2 -> 3
        1 2 -> 3
        """
        prev = None
        while k:
            next = head.next
            head.next = prev
            prev = head
            head = next
            k -= 1
        return prev

    if not head:
        return None

    node = head
    r_tail = None
    r_head = None

    while node:
        i = 0
        node = head

        while i < k and node:
            i += 1
            node = node.next

        if i == k:
            h = reverse(head, k)

            if not r_head:
                r_head = h
            if r_tail:
                r_tail.next = h
            r_tail = head
            head = node
    if r_tail:
        r_tail.next = head

    return r_head

# def review1(head: ListNode | None, k: int) -> ListNode | None:
#     def reverse(head, k):
#         prev = None
#         while k:
#             next = head.next
#             head.next = prev
#             prev = head
#             head = next
#             k -= 1

#         return prev

#     reversed_head = None
#     traversed = 0
#     reverse_start = None

#     while head:
#         if traversed == 0:
#             reverse_start = head

#         traversed += 1
#         head = head.next

#         if traversed == k:
#             node = reverse(reverse_start, k)
#             if not reversed_head:
#                 reversed_head = node
#             reverse_start.next = head
#             reverse_start = None
#             traversed = 0

#     return reversed_head
