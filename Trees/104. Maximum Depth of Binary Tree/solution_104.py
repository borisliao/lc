# Definition for a binary tree node.
from typing import Optional


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


def maxDepth(root: Optional[TreeNode]) -> int:
    """attempt 1, DFS, recursive"""
    if root:
        left_depth = 1 + maxDepth(root.left)
        right_depth = 1 + maxDepth(root.right)

        return max(left_depth, right_depth)

    return 0


def BFS(root: Optional[TreeNode]) -> int:
    """attempt 2, BFS, recursive, no queue (using lists)"""
    if not root:
        return 0

    left_nodes: list[TreeNode] = []
    right_nodes: list[TreeNode] = []
    if root.left:
        left_nodes.append(root.left)
    if root.right:
        right_nodes.append(root.right)

    count = 1
    while left_nodes or right_nodes:
        new_left = []
        for node in left_nodes:
            if node.left:
                new_left.append(node.left)
            if node.right:
                new_left.append(node.right)
        left_nodes = new_left

        new_right = []
        for node in right_nodes:
            if node.left:
                new_right.append(node.left)
            if node.right:
                new_right.append(node.right)
        right_nodes = new_right
        count += 1

    return count
