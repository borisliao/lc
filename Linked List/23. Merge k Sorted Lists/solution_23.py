class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        l = []

        def addToList(ln: ListNode, l: list):
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


def review3(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 2-3-24
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
        for i in range(0, len(lists)-interval, 2*interval):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]


def review5(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 2-5-24
    Time: 7 min
    Used: debugger 1
    """
    def merge(l, r):
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

    if not lists:  # d1
        return None  # d1

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists)-interval, 2*interval):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2
    return lists[0]


def review6(lists: list[ListNode | None]) -> ListNode | None:
    """
    Anki 2-15-24
    """
    def merge(l, r):
        if not l:
            return r
        if not r:
            return l
        if l.val < r.val:
            l.next = merge(l.next, r)
            return l
        else:
            r.next = merge(l, r.next)
            return r  # s3

    if not lists:  # s1
        return None  # s1

    interval = 1
    while interval < len(lists):  # s2
        for i in range(0, len(lists)-interval, 2*interval):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2  # s1 interval+1

    return lists[0]


def review7(lists: list[ListNode | None]) -> ListNode:
    """
    Mochi 4-14-24
    Time: 27:41
    Too slow
    """
    dummy = ListNode()
    node = dummy

    for i in range(len(lists)-1, -1, -1):  # Edge case
        if not lists[i] or lists[i].val == None:
            del lists[i]

    while lists:
        i: int = None
        smallest: ListNode = None
        for index, ln in enumerate(lists):
            if not smallest or ln.val < smallest.val:
                i = index
                smallest = ln
        node.next = smallest
        node = node.next
        lists[i] = lists[i].next
        if not lists[i]:
            del lists[i]
    return dummy.next


def review8(lists: list[ListNode | None]) -> ListNode:
    """
    Mochi 11-3-24
    Does not take advantage of the sorted lists
    """
    dummy = ListNode()
    head = dummy

    while lists:
        s = 0
        i = 0
        while i < len(lists):
            if lists[i].val == None:
                del lists[i]
            elif lists[i].val < lists[s].val:
                s = i
            else:
                i += 1
        if lists:

            head.next = lists[s]
            head = head.next
            lists[s] = lists[s].next
            if not lists[s] or lists[s].val == None:
                del lists[s]

    return dummy.next


def review9(lists: list[ListNode | None]) -> ListNode:
    """
    Mochi 11-3-24
    """
    def merge(l, r):
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
        for i in range(0, len(lists)-interval, 2*interval):
            lists[i] = merge(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]
