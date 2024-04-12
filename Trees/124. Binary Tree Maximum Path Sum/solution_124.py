# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
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


def maxPathSum(root: TreeNode | None) -> int:
    """
    Anki 2-2-24
    Used: https://www.youtube.com/watch?v=Hr5cWUld4vU
    """
    largest = root.val

    def dfs(root: TreeNode):
        nonlocal largest
        if not root:
            return 0

        l = max(dfs(root.left), 0)
        r = max(dfs(root.right), 0)
        m = root.val  # s3

        largest = max(largest, l+m+r)  # s1 max(l,m,r)
        return m + max(l, r)  # s2 l+m+r

    dfs(root)
    return largest


def review1(root: TreeNode | None) -> int:
    """
    Anki 2-3-24
    Time: 5:42
    Used: debugger 1
    """
    largest = root.val

    def dfs(root):
        nonlocal largest  # d1
        if not root:
            return 0

        l = max(0, dfs(root.left))
        r = max(0, dfs(root.right))
        m = root.val

        largest = max(largest, l+r+m)

        return m + max(l, r, 0)

    dfs(root)
    return largest


def review2(root: TreeNode | None) -> int:
    """
    Anki 2-3-24
    Used: solution
    """
    path = float('-inf')

    def dfs(n):
        nonlocal path
        if not n:
            return 0

        l = max(0, dfs(n.left))
        r = max(0, dfs(n.right))
        m = n.val

        path = max(path, l + m + r)

        return m + max(l, r, 0)

    dfs(root)
    return path


def review3(root: TreeNode | None) -> int:
    """
    Anki 2-13-24
    """
    result = float('-inf')

    def dfs(n):
        nonlocal result
        if not n:
            return 0
        l = max(0, dfs(n.left))
        r = max(0, dfs(n.right))
        m = n.val

        result = max(l+r+m, result)
        return max(m+l, m+r, 0)

    dfs(root)
    return result


def review4(root: TreeNode | None) -> int:
    """
    Anki 2-13-24
    Time: 7 min
    """
    result = float('-inf')

    def dfs(node):
        nonlocal result
        if not node:
            return 0
        l = max(0, dfs(node.left))
        r = max(0, dfs(node.right))
        m = node.val

        result = max(l+r+m, result)
        return m + max(l, r, 0)
    dfs(root)
    return result


def review5(root: TreeNode | None) -> int:
    """
    Mochi 4-11-24
    Time: 12 min
    """
    largest = float('-inf')  # d1 0

    def dfs(node: TreeNode):
        nonlocal largest
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        mid = node.val

        largest = max(largest, left+mid+right, left+mid, mid+right, mid)
        return max(left+mid, mid+right, mid)
    dfs(root)
    return largest
