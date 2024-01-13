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


def review1(head: Optional[Node]) -> Optional[Node]:
    """
    Anki 12-11-23
    Time: 1:36:57
    Used: Debugger (3)
    """
    node_map = {}

    new_head = Node(-1)  # dummy node

    node = head
    new_node = new_head

    while node:
        new_next_node = Node(node.val)
        node_map[node] = [node.random, new_next_node]  # d1
        new_node.next = new_next_node
        node = node.next
        new_node = new_node.next

    node = head
    new_node = new_head.next  # d2, d3

    while node:
        random_node = node_map[node][0]
        new_random_node = node_map[random_node][1] if random_node else None

        new_node.random = new_random_node

        node = node.next
        new_node = new_node.next

    return new_head.next


def review2(head: Optional[Node]) -> Optional[Node]:
    """
    Anki 12-11-23
    Time: 9 min
    Used: Solution (1)
    """
    new_head: dict[Node, Node] = {None: None}

    n = head
    while n:
        new_head[n] = Node(n.val)
        n = n.next

    n = head
    while n:
        new_head[n].next = new_head[n.next]  # s1
        new_head[n].random = new_head[n.random]
        n = n.next

    return new_head[head]


def review3(head: Optional[Node]) -> Optional[Node]:
    """
    Anki 12-22-23
    Time: 18:34
    Used: Debugger 1
    """
    new_head = Node(-1)
    dummy = new_head
    h = head

    new_node: dict[Node: Node] = {None: None}  # d1 forgot None: None

    while h:
        new_node[h] = Node(h.val)
        dummy.next = new_node[h]
        dummy = dummy.next
        h = h.next

    h = head
    dummy = new_head.next
    while h:
        dummy.random = new_node[h.random]
        dummy = dummy.next
        h = h.next

    return new_head.next


def review4(head: Optional[Node]) -> Optional[Node]:
    """
    12-22-23
    Time: 11:46
    Used: Debugger 3
    """

    new_node: dict[Node, Node] = {None: None}
    h = head  # d1
    while h:
        new_node[h] = Node(h.val)
        h = h.next  # d1

    h = head
    while h:
        new_node[h].random = new_node[h.random]  # d3
        new_node[h].next = new_node[h.next]  # d2
        h = h.next

    return new_node[head]


def review5(head: Node | None) -> Node | None:
    """
    Anki 1-12-24
    Time: 6 min
    Used: Debugger 1
    """
    new_node: dict[Node, Node] = {None: None}
    n = head
    while n:
        new_node[n] = Node(n.val)
        n = n.next  # d1

    n = head
    while n:
        new_node[n].next = new_node[n.next]
        new_node[n].random = new_node[n.random]
        n = n.next  # d1

    return new_node[head]


# def review6(head: Node | None) -> Node | None:
#     """
#     Anki 1-12-24
#     """
