from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """
        Source: https://stackoverflow.com/questions/37495634/python-list-from-python-binary-tree
        """
        items = []
        queue = [self]

        while queue:
            copy = queue[:]
            queue = []

            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    items.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)

            if all((x is None for x in queue)):
                break

        return str(items)

    def __repr__(self):
        return f"{self}"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)

    def __hash__(self):
        return id(self)


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    level_nodes = [root]
    node_values = []
    while level_nodes:
        new_level_nodes = []
        new_node_values = []
        for node in level_nodes:
            new_node_values.append(node.val)
            if node.left:
                new_level_nodes.append(node.left)
            if node.right:
                new_level_nodes.append(node.right)
        level_nodes = new_level_nodes
        node_values.append(new_node_values)

    return node_values


def review1(root: TreeNode | None) -> list[list[int]]:
    """
    Anki 12-24-23
    Time: 18 min
    Used: Debugger 2
    """
    result = []
    stack: deque[TreeNode] = deque()  # d2 used deque for o(n) pop

    if root:
        stack.append(root)

    while stack:
        layer = []
        for _ in range(len(stack)):
            value = stack.popleft()  # d2 used deque for o(n) pop
            # d1 value instead of value.val (did not read question)
            layer.append(value.val)
            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)

        result.append(layer)

    return result
