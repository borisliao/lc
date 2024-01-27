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


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(n, l, r):
        if n is None:
            return True
        if l < n.val < r:
            return dfs(n.left, l, n.val) and dfs(n.right, n.val, r)
        return False
    return dfs(root, float('-inf'), float('inf'))


# def review1(root: TreeNode) -> bool:
#     """
#     Anki 1-21-24
#     Time: 6 min
#     """
#     if not root:
#         return True

#     left_val = root.left.val if root.left else float('-inf')
#     right_val = root.right.val if root.right else float('inf')

#     if left_val < root.val < right_val:  # d1 root
#         return review1(root.left) and review1(root.right)

#     return False

def review2(root: TreeNode) -> bool:
    """
    Anki 1-21-24
    Time: 25 min
    Used: [Validate Binary Search Tree - Depth First Search - Leetcode 98](https://www.youtube.com/watch?v=s6ATEkipzow)
    """
    def dfs(root: TreeNode | None, l: int, r: int):
        if not root:
            return True
        if l < root.val < r:
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        return False
    return dfs(root, float('-inf'), float('inf'))


def review3(root: TreeNode) -> bool:
    """
    Anki 1-21-24
    Time: 4 min
    """
    def dfs(root: TreeNode | None, l: int, r: int):
        if not root:
            return True
        elif l < root.val < r:
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        return False
    return dfs(root, float('-inf'), float('inf'))


def review4(root: TreeNode) -> bool:
    """
    Anki 1-27-24
    Time: 5 min
    """
    def dfs(root, l, r):
        if not root:
            return True
        if l < root.val < r:
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        return False

    return dfs(root, float('-inf'), float('inf'))

# def review6(root: TreeNode) -> bool:
#     """
#     Anki 1-27-24
#     Time: 5 min
#     """
