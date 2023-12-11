from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        li: list[list] = []
        node_placement = {None: None}

        n = self
        i = 0
        while n:
            li.append([n.val])
            node_placement[n] = i
            n = n.next
            i += 1

        n = self

        for l in li:
            l.append(node_placement[n.random])
            n = n.next

        return str(li)

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)

    def __hash__(self):
        return id(self)


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    headDict = {None: None}

    cur = head
    while cur:
        headDict[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        headDict[cur].next = headDict[cur.next]
        headDict[cur].random = headDict[cur.random]
        cur = cur.next

    return headDict[head]
