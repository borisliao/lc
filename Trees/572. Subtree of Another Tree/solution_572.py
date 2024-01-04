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


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """Solved with neetcode: https://www.youtube.com/watch?v=E36O5SWp-LE"""
    def isSameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a == None and b == None:
            return True
        if a and b and (a.val == b.val):
            return (isSameTree(a.left, b.left) and isSameTree(a.right, b.right))
        return False

    if root and subRoot == None:
        return True
    if root == None and subRoot:
        return False
    if root.val == subRoot.val:
        if isSameTree(root, subRoot):
            return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def review1(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    """
    Anki 1-4-24
    Used: [Subtree of Another Tree - Leetcode 572 - Python](https://www.youtube.com/watch?v=E36O5SWp-LE)
    """
    def sameTree(a, b):
        if a == None and b == None:
            return True
        elif a and b and a.val == b.val:
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)
        else:
            return False

    def dfs(r, st):
        if r == None and st == None:
            return True
        elif r == None and st:
            return False
        elif r and st and r.val == st.val:
            if sameTree(r, st):
                return True
        return dfs(r.left, st) or dfs(r.right, st)

    return dfs(root, subRoot)
