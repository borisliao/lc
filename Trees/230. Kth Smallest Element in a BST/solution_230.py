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


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    c = root

    while stack or c:
        while c:
            stack.append(c)
            c = c.left

        c = stack.pop()
        k -= 1
        if k == 0:
            return c.val
        c = c.right


# def review1(root: TreeNode | None, k: int) -> int:
#     """
#     Anki 1-22-24
#     Time: 24 min
#     """
#     smallest = None

#     def dfs(root: TreeNode | None, k: int):
#         nonlocal smallest  # d2
#         if not root or smallest:
#             return k
#         if root.left:
#             k = dfs(root.left, k)
#         if k > 0:
#             dfs(root.right, k-1)
#             return k-1
#         elif k == 0:
#             smallest = root.val
#             return k  # d2
#     dfs(root, k)  # d1
#     return smallest


# def review2 (root: TreeNode | None, k: int) -> int:
#     """
#     Anki 1-22-24
#     """
#     stack = [root]

#     while stack:
#         n = stack.pop()
#         k -= 1
#         if k == 0:
#             return n.val
#         if n.right:
#             stack.append(n.right)
#         if n.left:
#             stack.append(n.left)

def review3(root: TreeNode | None, k: int) -> int:
    """
    Anki 1-22-24
    """
    stack = []
    c = root

    while stack or c:
        while c:
            stack.append(c)
            c = c.left
        c = stack.pop()
        k -= 1
        if k == 0:
            return c.val
        c = c.right


def review4(root: TreeNode | None, k: int) -> int:
    """
    Anki 1-24-24
    """
    stack = []
    c = root
    while stack or c:
        while c:
            stack.append(c)
            c = c.left
        c = stack.pop()
        k -= 1
        if k == 0:
            return c.val
        c = c.right
