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


# def attempt1(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0

#     def depth(r: Optional[TreeNode]) -> int:
#         if not r:
#             return 0

#         l_len = 0
#         if r.left:
#             l_len = 1 + depth(r.left)

#         r_len = 0
#         if r.right:
#             r_len = 1 + depth(r.right)

#         return max(l_len, r_len)

#     l_len = 0
#     if root.left:
#         l_len = 1

#     r_len = 0
#     if root.right:
#         r_len = 1

#     return l_len + depth(root.left) + r_len + depth(root.right)


# def attempt2(root: Optional[TreeNode]) -> int:
#     """Hint from neetcode: https://www.youtube.com/watch?v=bkxqA8Rfv04"""
#     if not root:
#         return 0
#     max_diameter = 0

#     def depth(r: Optional[TreeNode]) -> int:
#         nonlocal max_diameter
#         if not r:
#             return 0

#         l_len = 0
#         if r.left:
#             l_len = 1 + depth(r.left)

#         r_len = 0
#         if r.right:
#             r_len = 1 + depth(r.right)

#         l_len = 0
#         if root.left:
#             l_len = 1

#         r_len = 0
#         if root.right:
#             r_len = 1

#         current_diameter = l_len + depth(root.left) + r_len + depth(root.right)
#         max_diameter = max(max_diameter, current_diameter)
#         return max(l_len, r_len)

#     return max_diameter

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """Solution from Neetcode
    https://github.com/neetcode-gh/leetcode/blob/main/python/0543-diameter-of-binary-tree.py
    and Youtube comment
     [![@Obligedcartoon](https://yt3.ggpht.com/ytc/AOPolaSuwO7TFa7NhT3M5utOb_dzeUiiOT9IKyryAxCO98D1fOArQBy497XZ8gLbpoaS=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/channel/UCoSrg3IhP3gxUUM2tpi-D0Q) 

    ### [@Obligedcartoon](https://www.youtube.com/channel/UCoSrg3IhP3gxUUM2tpi-D0Q)

    [1 year ago](https://www.youtube.com/watch?v=bkxqA8Rfv04&lc=Ugz_eKAW4v617vBGVvZ4AaABAg)

    Alternative mathematical approach: It made a little more sense to me to return 0 for a Null node. In doing so, you don't need the + 2 in the updating of the result. You are essentially accounting for the parent edge in different ways. I found this approach to come a little more naturally to me, so I'm posting in case it helps anyone!
    """
    res = 0

    def dfs(root: Optional[TreeNode]):
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res


def review1(root: TreeNode | None) -> int:
    """
    Anki 1-3-24
    Used: Solution 1
    Time: 15 min
    """
    largest = 0

    def dfs(node: TreeNode | None):
        nonlocal largest
        if node == None:
            return 0

        left_depth = dfs(node.left)  # s1 1 + dfs(node.left)
        right_depth = dfs(node.right)  # s1 1 + dfs(node.left)

        largest = max(left_depth + right_depth, largest)
        return 1 + max(left_depth, right_depth)  # s1 missing 1 +

    dfs(root)
    return largest


def review2(root: TreeNode | None) -> int:
    """
    Anki 1-7-24
    Time: 12 min
    Used: debugger 2
    """
    max_diameter = 0

    def dfs(root: TreeNode | None):
        nonlocal max_diameter
        if root == None:
            return 0
        left_depth = dfs(root.left)
        right_depth = dfs(root.right)

        # d1 forgot , max_diameter
        max_diameter = max(left_depth + right_depth, max_diameter)
        return 1 + max(left_depth, right_depth)

    dfs(root)  # d2
    return max_diameter


def review3(root: TreeNode) -> int:
    """
    Anki 1-16-24
    Time: 10 min
    """
    diameter = 0

    def dfs(node: TreeNode):
        nonlocal diameter
        if not node:
            return 0

        left_length = 1 + dfs(node.left) if node.left else 0
        right_length = 1 + dfs(node.right) if node.right else 0

        diameter = max(left_length + right_length, diameter)

        return max(left_length, right_length)

    dfs(root)  # d1
    return diameter  # d1


def review4(root: TreeNode) -> int:
    """
    Mochi 4-7-24
    Time: 20 min
    """
    max_length = 0

    def dfs(node: TreeNode):
        nonlocal max_length
        if not node:
            return 0
        left = 1 + dfs(node.left) if node.left else 0
        right = 1 + dfs(node.right) if node.right else 0

        max_length = max(max_length, left+right)

        return max(left, right)  # s1

    dfs(root)
    return max_length
