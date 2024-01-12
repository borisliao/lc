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


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    """
    Uses BFS to traverse all the nodes, and pick the right most node
    """
    if not root:
        return []

    stack = [root]
    result = []
    while stack:
        result.append(stack[-1].val)
        new_stack = []
        for node in stack:
            if node.left:
                new_stack.append(node.left)
            if node.right:
                new_stack.append(node.right)
        stack = new_stack

    return result


def review1(root: TreeNode | None) -> list[int]:
    """
    Anki 12-29-23
    Used: Solution, debugger 2
    Time: 20 min
    """
    stack = deque([root]) if root else None
    right_nodes = [root.val] if root else []

    new_stack = []
    while stack or new_stack:
        if not stack and new_stack:
            right_nodes.append(new_stack[-1].val)
            stack.extend(new_stack)  # d1 append
            new_stack = []  # d2
        n = stack.popleft()
        if n.left:
            new_stack.append(n.left)
        if n.right:
            new_stack.append(n.right)

    return right_nodes


def review2(root: TreeNode | None) -> list[int]:
    """
    Anki 12-29-23
    Time: 15 min
    Used: [Binary Tree Right Side View - Breadth First Search - Leetcode 199](https://www.youtube.com/watch?v=d4zLyf32e3I)
    """
    stack = deque([root])  # d1 [root]
    result = []
    while stack:
        last_node = None
        next_layer = deque()  # d2
        for n in stack:
            last_node = n
            if n:  # s3 n
                next_layer.append(n.left)
                next_layer.append(n.right)
        if last_node:  # s3
            result.append(last_node.val)  # s3

        stack = next_layer  # d2
    return result


def review3(root: TreeNode | None) -> list[int]:
    """
    Anki 12-29-23
    """
    stack = deque([root])
    result = []
    while stack:
        next_layer = deque()
        last_node = None
        for n in stack:
            if n:
                last_node = n
                next_layer.append(n.left)
                next_layer.append(n.right)
        if last_node:
            result.append(last_node.val)  # d1 .val
        stack = next_layer

    return result


def review4(root: TreeNode | None) -> list[int]:
    """
    Anki 1-1-24
    Time: 8 min
    Used: debugger 1
    """
    stack = [root] if root else []
    result = [root.val] if root else []  # d1

    new_stack = []
    while stack:
        for n in stack:
            if n.left:
                new_stack.append(n.left)
            if n.right:
                new_stack.append(n.right)

        if new_stack:
            result.append(new_stack[-1].val)

        stack = new_stack
        new_stack = []

    return result


def review5(root: TreeNode | None) -> list[int]:
    """
    Anki 1-12-24
    Time: 4 min
    """
    stack = [root] if root else []
    result = []

    while stack:
        result.append(stack[-1].val)
        new_stack = []
        for n in stack:
            if n.left:
                new_stack.append(n.left)
            if n.right:
                new_stack.append(n.right)
        stack = new_stack

    return result
