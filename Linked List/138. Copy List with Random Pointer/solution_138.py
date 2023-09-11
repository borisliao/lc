from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        list = []
        random_list = []

        def addToList(ln: Node, list: List):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        def randomAddToList(ln: Node, list: List):
            list.append(ln.val)
            if (ln.random):
                addToList(ln.random, list)
        randomAddToList(self, random_list)

        return str(list) + str(random_list)

    def __repr__(self):
        return f"({self.val}, {self.next}, {self.random})"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    pass
