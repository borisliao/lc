class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: 'list'):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __repr__(self):
        return f"({self.val}, {self.next})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


def attempt1(head: ListNode | None) -> ListNode | None:
    """
    Done by creating a new ListNode. Not very space efficent.
    1-1-23
    """
    if head and head.val != None:
        result = ListNode(val=head.val)
        head = head.next

        while head:
            result = ListNode(val=head.val, next=result)
            head = head.next

        return result
    else:
        return head


def attempt2(head: ListNode | None) -> ListNode | None:
    """
    Done without using extra space complexity and iteratively.
    Same as how NeetCode did it
    1-1-23
    """
    prev, curr = None, head

    while curr:
        curr_next = curr.next
        curr.next = prev

        prev = curr
        curr = curr_next

    return prev


def youtubeCommentRecursively(head: ListNode | None) -> ListNode | None:
    """
        [![@Extremesarova](https://yt3.ggpht.com/ytc/AOPolaSUgkJ9T7zraqMY4MFRnye0LpCc0DCST5gsKBDicA=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/channel/UC4lk9BCGbIaaz2nn5PmpezQ)
        [@Extremesarova](https://www.youtube.com/channel/UC4lk9BCGbIaaz2nn5PmpezQ)
        [1 year ago (edited)](https://www.youtube.com/watch?v=G0_I-ZF0S38&lc=UgzJCGMTagZa7I5K9GN4AaABAg)

        Maybe this recursive solution can make things clearer for you, guys <code below...>
        Also, I think that we are using three pointers here: prev, cur and next.
    """
    def reverse(cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

    return reverse(head, None)


def neetCodeRecursively(head: ListNode | None) -> ListNode | None:
    """https://youtu.be/G0_I-ZF0S38?si=li7NQdrD4EcPvNZC&t=647"""
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = neetCodeRecursively(head.next)
        head.next.next = head
    head.next = None

    return newHead


def review1(head):
    """
    Mochi 4-21-24
    """
    prev = None
    node = head

    while node:
        next = node.next

        node.next = prev
        prev = node

        node = next

    return prev


def review2(head):
    """
    Mochi 4-22-24
    """
    prev = None
    node = head
    while node:
        next = node.next

        node.next = prev
        prev = node

        node = next

    return prev


def review3(head: ListNode | None) -> ListNode | None:
    """
    Mochi 4-24-24
    """
    prev = None

    while head:
        next = head.next

        head.next = prev
        prev = head

        head = next

    return prev


def review4(head: ListNode | None) -> ListNode | None:
    """
    Mochi 6-26-24
    """
    prev = None

    node = head
    while node:
        next = node.next
        node.next = prev
        prev = node  # d1
        node = next

    return prev


def review_lc25_1(head: ListNode):
    """
    Mochi 11-18-24
    Reviewed as part of the solution of 25. Reverse Nodes in k-Group
    """
    prev = None
    node = head

    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev


def review_lc25_2(head: ListNode):
    """
    Mochi 11-18-24
    Reviewed as part of the solution of 25. Reverse Nodes in k-Group
    """
    def reverse(head: ListNode, prev: ListNode):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return reverse(next, head)
    return reverse(head, None)
