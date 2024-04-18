class TreeNode:
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
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
    Anki 1-2-24
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


def review3(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 1-8-24
    Time: 15 min
    Alternative solution declaring explicit condition
    Used: debugger 1, solution 1
    """
    if (root.val > p.val and root.val < q.val
        or root.val <= p.val and root.val >= q.val  # s1
            or root.val == p.val or root.val == q.val):
        return root
    elif root.val < p.val and root.val < q.val:
        return review2(root.right, p, q)  # d1 p, q
    elif root.val > p.val and root.val > q.val:
        return review2(root.left, p, q)  # d1 p, q


def review4(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 1-8-24
    Time: 17 min
    Used: debugger 1
    """
    if root.val < p.val and root.val < q.val:
        return review3(root.right, p, q)  # d1 p, q
    elif root.val > p.val and root.val > q.val:
        return review3(root.left, p, q)  # d1 p, q
    else:
        return root


def review5(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 1-22-24
    Time: 16 min
    Used: Solution 1
    """
    if root.val < p.val and root.val < q.val:
        return review4(root.right, p, q)  # s1 root.left
    elif root.val > p.val and root.val > q.val:
        return review4(root.left, p, q)  # s1 root.right
    else:
        return root


def review6(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Anki 2-9-24
    Time: 8 min
    """
    if root.val < p.val and root.val < q.val:
        return review5(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return review5(root.left, p, q)
    else:
        return root


def review7(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Mochi 4-18-24
    """
    # covers the root.val == p.val or root.val == q.val case
    # and the root.val > p.val and root.val < q.val case
    # and the root.val < p.val and root.val > q.val case
    if ((p.val < root.val and root.val < q.val)
        or (q.val < root.val and root.val < p.val)
            or (root.val == p.val)
            or (root.val == q.val)):
        return root
    elif p.val < root.val and q.val < root.val:
        return review7(root.left, p, q)
    else:
        return review7(root.right, p, q)
