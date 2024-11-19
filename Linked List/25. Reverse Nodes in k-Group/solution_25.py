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
    """
    Cracking FAANG
    https://www.youtube.com/watch?v=ug6nP_thrsw
    """
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


def review1(head: ListNode | None, k: int) -> ListNode | None:
    def reverse(head, k):
        prev = None
        while k:
            next = head.next
            head.next = prev
            prev = head
            head = next
            k -= 1

        return prev

    node = head
    prev_tail = None
    new_head = None

    while node:
        traversed = 0
        traversed_head = node

        while traversed < k and node:
            node = node.next
            traversed += 1

        if traversed == k:
            reversed_head = reverse(traversed_head, k)

            if not new_head:  # runs only one time
                new_head = reversed_head

            if prev_tail:  # connect the prev traversed tail to the new reversed head
                prev_tail.next = reversed_head

            prev_tail = head
            head = node
        elif traversed < k:
            prev_tail.next = head

    return new_head if new_head else head


def review3(head: ListNode | None, k: int) -> ListNode | None:
    """
    Anki 2-5-24
    Time: 20 min
    """
    def reverse(h, k):
        prev = None
        while k:
            n = h.next
            h.next = prev
            prev = h
            h = n
            k -= 1
        return prev
    prev_tail = None
    new_head = None
    while head:
        t = head
        distance = 0

        while t and distance < k:
            t = t.next
            distance += 1

        if distance == k:
            reversed_head = reverse(head, k)

            if not new_head:
                new_head = reversed_head

            if prev_tail:
                prev_tail.next = reversed_head

            prev_tail = head
            head = t
        elif distance < k:
            prev_tail.next = head
            break  # d1

    return new_head


def review4(head: ListNode | None, k: int) -> ListNode | None:
    """
    Anki 2-6-24
    Time: 12 min
    """
    def reverse(h, k):
        prev = None
        while k:
            n = h.next
            h.next = prev
            prev = h
            h = n
            k -= 1
        return prev

    prev_tail = None
    new_head = None
    traversed = 0
    while head:  # only covers when len(head) % k == 0
        t = head
        while t and traversed < k:
            t = t.next
            traversed += 1

        if traversed == k:
            reversed_head = reverse(head, k)

            if not new_head:  # only runs one time
                new_head = reversed_head

            if prev_tail:
                prev_tail.next = reversed_head

            prev_tail = head
            traversed = 0
            head = t
        elif traversed < k:
            prev_tail.next = head
            break

    return new_head


def review5(head: ListNode, k: int) -> ListNode:
    """
    Mochi 11-18-24
    """
    def reverse(head: ListNode, k: int):
        prev = None
        node = head

        while k:
            next = node.next
            node.next = prev
            prev = node
            node = next
            k -= 1
        return prev

    prev = None
    node = head

    new_head = None

    while node:
        count = 0
        node = head

        # check if we have k elements to reverse
        while count < k and node:
            node = node.next
            count += 1

        # if k elements do exist
        if count == k:
            rev_head = reverse(head, k)

            if not new_head:
                new_head = rev_head
            if prev:
                prev.next = rev_head
            prev = head
            head = node
    if prev:
        prev.next = head

    return new_head if new_head else head
