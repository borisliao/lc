# Definition for a binary tree node.
from collections import deque
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


def isBalanced(root: Optional[TreeNode]) -> bool:
    """
    Solution from neetcode: https://www.youtube.com/watch?v=QfJsau0ItOY
    """
    def dfs(tn: Optional[TreeNode]):
        if tn is None:
            return {"unbalanced": True, "length": 0}

        left, right = dfs(tn.left), dfs(tn.right)
        weight_difference = abs(left['length'] - right['length'])

        balanced_state = weight_difference <= 1 and left['unbalanced'] and right['unbalanced']
        return {"unbalanced": balanced_state, "length": 1 + max(left['length'], right['length'])}

    return dfs(root)['unbalanced']


def globalVar(root: Optional[TreeNode]) -> bool:
    """
    Solution from neetcode: https://www.youtube.com/watch?v=QfJsau0ItOY
    """
    isUnbalanced = False

    def dfs(tn: Optional[TreeNode]):
        nonlocal isUnbalanced
        if tn is None:
            isUnbalanced = True
            return 0

        left, right = dfs(tn.left), dfs(tn.right)
        weight_difference = abs(left - right)

        balanced_state = weight_difference < 1
        if balanced_state:
            isUnbalanced = True

        return 1 + max(left, right)

    dfs(root)
    return isUnbalanced
