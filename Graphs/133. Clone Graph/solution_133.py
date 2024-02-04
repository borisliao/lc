
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __hash__(self) -> int:
        return id(self)


def neetcode(node: Node | None) -> Node | None:
    """
    Anki 2-3-24
    Used: https://www.youtube.com/watch?v=mQeF6bN8hMk
    DFS
    """
    if not node:
        return None

    clone = {}

    def dfs(node: Node):
        if node in clone:
            return clone[node]

        copy = Node(node.val)
        clone[node] = copy

        for n in node.neighbors:
            copy.neighbors.append(dfs(n))
        return copy

    return dfs(node)


def crackingFaang(node: Node | None) -> Node | None:
    """
    Anki 2-3-24
    Used: https://www.youtube.com/watch?v=vXkT2nYSde0
    BFS
    """
    if not node:
        return None

    clone = {}
    clone[node] = Node(node.val, [])

    q = deque(node)
    q.append(node)

    while q:
        cur = q.popleft()

        for neighbor in cur.neighbors:
            if neighbor not in clone:
                clone[neighbor] = Node(neighbor.val, [])
                q.append(neighbor)
            clone[cur].neighbors.append(clone[neighbor])

    return clone[node]


def review1(node: Node | None) -> Node | None:
    """
    Anki 2-3-24
    Used: Solution 1
    Time: 8 min
    """
    clone = {}

    if not node:
        return None

    def dfs(node: Node):
        if node in clone:
            return clone[node]
        copy = Node(node.val, [])
        clone[node] = copy

        for n in node.neighbors:
            copy.neighbors.append(dfs(n))  # s1
        return copy

    return dfs(node)


def review2(node: Node | None) -> Node | None:
    """
    Anki 2-4-24
    Time: 13 min
    Used: Solution 4
    """
    if not node:  # s4
        return None  # s4
    clones = {node: Node(node.val, [])}  # s3 optimization {}

    q = deque([node])  # d1 deque(node)

    while q:
        n = q.popleft()
        # s3 optimization
        # if n not in clones:
        #     clones[n] = Node(n.val, [])
        for neighbor in n.neighbors:
            if neighbor not in clones:
                q.append(neighbor)  # s2 up 1
                clones[neighbor] = Node(neighbor.val, [])
            clones[n].neighbors.append(clones[neighbor])

    return clones[node]
