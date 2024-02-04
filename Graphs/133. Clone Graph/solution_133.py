
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
