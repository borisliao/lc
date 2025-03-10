class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
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

def attempt1(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    Done with NeetCode guide: https://www.youtube.com/watch?v=S5bfdUTrKLM
    """
    # -----find middle-----
    # [1, 2, 3, 4, 5]
    if head.next == None:
        return
    # slow, fast pointers
    slow, fast = head, head.next  # [1, 2, 3, 4, 5] [2, 3, 4, 5]

    while fast and fast.next:
        slow = slow.next  # [2, 3, 4, 5],
        fast = fast.next.next  # [3, 4, 5],

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
        l1_next = l1.next  # [2, 3], [3]
        l2_next = l2.next  # [4], None

        l1.next = l2  # [1, 5, 4], [3, 4]
        l2.next = l1_next  # [1, 5, 2, 3], [None]

        l1 = l1_next  # [2, 3], [3]
        l2 = l2_next  # [4], None


def neetcode(head: ListNode) -> None:
    """
    https://www.youtube.com/watch?v=S5bfdUTrKLM
    """
    # find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# def review1(head: ListNode) -> None:
#     """
#     Anki 12-13-23
#     """
#     even: list[ListNode] = []
#     odds: list[ListNode] = []

#     i = 0
#     while head:
#         state = 'odd' if i % 2 == 1 else 'even'
#         if state == 'odd':
#             odds.append(head)
#         else:
#             even.append(head)
#         head = head.next
#         i += 1

#     i = 0
#     while odds or even:
#         if even[0]:
#             even[0].next


def review2(head: ListNode) -> None:
    """
    Anki 12-14-23
    """
    # find midpoint
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second half
    second_half = slow.next

    slow.next = None
    node = second_half
    prev_node = None
    while node:
        temp_node = node.next
        node.next = prev_node
        prev_node = node
        node = temp_node

    # merge lists
    first_half = head
    second_half = prev_node  # s3

    while second_half:  # s2 was first_half
        temp1, temp2 = first_half.next, second_half.next  # s1
        first_half.next = second_half  # s1
        second_half.next = temp1  # s1

        first_half, second_half = temp1, temp2  # s1

    return head


def review3(head: ListNode) -> None:
    """
    Anki 12-18-23
    Used: Solution 4
    Time: 32:54
    """
    # find midpoint #s1
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse midpoint
    second_half = slow.next

    slow.next = None
    node = second_half
    prev = None
    while node:
        temp_node = node.next
        node.next = prev
        prev = node  # s2
        node = temp_node

    # Merge lists
    l1 = head
    l2 = prev  # s4 next to prev

    while l2:
        temp1, temp2 = l1.next, l2.next  # s3
        l1.next = l2  # s3
        l2.next = temp1  # s3

        l1, l2 = temp1, temp2  # s3

    return head


def review4(head: ListNode) -> None:
    """
    Anki 12-18-23
    Walk through review
    """
    # Find Midpoint
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse Second Half
    second_half = slow.next

    slow.next = None  # break link

    node = second_half
    prev_node = None

    while node:
        temp_node = node.next
        node.next = prev_node
        prev_node = node
        node = temp_node

    # Merge Lists
    l1 = head
    l2 = prev_node

    while l2:
        temp1, temp2 = l1.next, l2.next
        l1.next = l2
        l2.next = temp1

        l1, l2 = temp1, temp2

    return head


def review5(head: ListNode) -> None:
    """
    Anki 12-18-23
    Time: 27:47
    Used: debugger 2
    """
    # find midpoint
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second list
    midpoint = slow.next
    slow.next = None

    prev = None
    node = midpoint  # d2 head -> node (name conflict)
    while node:
        temp1 = node.next
        node.next = prev
        prev = node  # d1
        node = temp1

    # merge two lists
    l1 = head
    l2 = prev

    while l2:
        t1 = l1.next
        t2 = l2.next

        l1.next = l2
        l2.next = t1

        l1 = t1
        l2 = t2

    return head


def review6(head: ListNode) -> None:
    """
    Anki 1-1-24
    Time: 20 min
    """
    # find midpoint
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse midpoint
    mid = slow.next
    slow.next = None

    prev = None
    node = mid
    while node:
        next_node = node.next
        node.next = prev

        prev = node
        node = next_node

    # merge lists
    first = head
    second = prev
    while second:
        next_first = first.next
        first.next = second

        first = next_first

        next_second = second.next
        second.next = first

        second = next_second


def review7(head: ListNode) -> None:
    """
    Anki 3-29-24
    Time: 15 min
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next  # s1
    slow.next = None  # s1

    prev = None  # s1
    node = mid
    while node:  # s1
        next_node = node.next  # s1
        node.next = prev  # s1

        prev = node  # s1
        node = next_node  # s1

    # merge lists # s1
    first = head  # s1
    second = prev  # s1
    while second:  # s1
        next_first = first.next  # s1
        first.next = second  # s1

        first = next_first  # s1

        next_second = second.next  # s1
        second.next = first  # s1

        second = next_second  # s1


def review8(head: ListNode) -> None:
    """
    Mochi 4-19-24
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    l = head
    r = slow.next
    slow.next = None

    prev = None
    node = r
    while node:
        next = node.next
        node.next = prev

        prev = node
        node = next

    r = prev

    while r:
        ln = l.next
        rn = r.next

        l.next = r
        r.next = ln

        l = ln
        r = rn

    return head


def review9(head: ListNode) -> None:
    """
    Mochi 4-20-24
    Time: 15:23
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    l = head
    r = slow.next
    slow.next = None

    prev = None
    node = r
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next

    r = prev

    while r:
        ln = l.next
        rn = r.next

        l.next = r
        r.next = ln

        r = rn
        l = ln


def review10(head: ListNode) -> None:
    """
    Mochi 4-22-24
    """
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    l = head
    r = slow.next
    slow.next = None

    prev = None
    while r:
        next = r.next

        r.next = prev
        prev = r

        r = next
    r = prev

    while r:
        ln = l.next
        rn = r.next

        l.next = r
        r.next = ln

        l = ln
        r = rn


def review11(head: ListNode) -> None:
    """
    Mochi 6-23-24
    """
    f = head
    s = head
    while f and f.next:
        f = f.next.next
        s = s.next

    n = s.next
    s.next = None
    prev = None
    while n:
        next = n.next

        n.next = prev
        prev = n

        n = next
    r = prev

    l = head
    while r:
        ln = l.next
        rn = r.next

        l.next = r
        r.next = ln

        l = ln
        r = rn
