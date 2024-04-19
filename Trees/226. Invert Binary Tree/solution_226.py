# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return root
    if root.left or root.right:
        leftSide = root.left
        root.left = root.right
        root.right = leftSide

        invertTree(root.left)
        invertTree(root.right)

    return root


def review1(root: TreeNode | None) -> TreeNode | None:
    """
    Anki 1-1-24
    Time: 13 min
    """
    def dfs(node: TreeNode | None):
        if node == None:
            return
        dfs(node.left)
        dfs(node.right)
        node.left, node.right = node.right, node.left

    dfs(root)
    return root


def review2(root: TreeNode | None) -> TreeNode | None:
    """
    Anki 1-6-24
    Time: 2 min
    """
    if root:
        review1(root.left)
        review1(root.right)
        root.left, root.right = root.right, root.left

    return root


def review3(root: TreeNode | None) -> TreeNode | None:
    """
    Anki 1-6-24
    Time: 4 min
    """
    if not root:
        return
    root.left, root.right = root.right, root.left
    review3(root.left)
    review3(root.right)

    return root


def review4(root: TreeNode | None) -> TreeNode | None:
    """
    Mochi 4-19-24
    Time: 2 min
    """
    if not root:
        return None
    root.left, root.right = review4(root.right), review4(root.left)
    return root
