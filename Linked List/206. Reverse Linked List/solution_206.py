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


def attempt1(head: Optional[ListNode]) -> Optional[ListNode]:
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


def attempt2(head: Optional[ListNode]) -> Optional[ListNode]:
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


def youtubeCommentRecursively(head: Optional[ListNode]) -> Optional[ListNode]:
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


def neetCodeRecursively(head: Optional[ListNode]) -> Optional[ListNode]:
    """https://youtu.be/G0_I-ZF0S38?si=li7NQdrD4EcPvNZC&t=647"""
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = neetCodeRecursively(head.next)
        head.next.next = head
    head.next = None

    return newHead
