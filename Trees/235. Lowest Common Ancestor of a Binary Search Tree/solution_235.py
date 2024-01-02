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


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    https://www.youtube.com/watch?v=gs2LMfuOR9k
    Use the binary tree structure to inform if the current node is the lowest common ancestor (LCA)
    If the root node value is both greater then p and q, then the LCA is in the left subtree
    If the root node value is both less then p and q, then the LCA is in the right subtree
    If the root node value is equal to any one of p or q, then the LCA has to be the root node
    If only one value is greator or less than p or q (aka subtree diverges), then the LCA has to be the root node
    """
    while root:
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            # covers the root.val == p.val or root.val == q.val case
            # and the root.val > p.val and root.val < q.val case
            # and the root.val < p.val and root.val > q.val case
            return root


def review1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 1-2-24
    Used: debugger 2
    Time: 28 min
    """
    p_path = []
    q_path = []

    path = []

    def dfs(node: TreeNode):
        nonlocal p_path, q_path

        path.append(node)
        if node.val == p.val:
            p_path = path.copy()
            # d1 returned
        if node.val == q.val:
            q_path = path.copy()
            # d1 returned

        if node.left:  # d2 popped when empty
            dfs(node.left)
            path.pop()
        if node.right:  # d2 popped when empty

            dfs(node.right)
            path.pop()

    dfs(root)

    lowest_node = None
    q_path = set(q_path)
    for p in p_path:
        if p in q_path:
            lowest_node = p

    return lowest_node


def review2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 1-2-23
    NOTE: use the fact that the data structure is a binary search tree, not a binary tree
    A binary search tree puts the lowest values on the left nodes
    """
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
