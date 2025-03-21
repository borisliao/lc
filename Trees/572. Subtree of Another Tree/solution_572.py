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


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    """Solved with neetcode: https://www.youtube.com/watch?v=E36O5SWp-LE"""
    def isSameTree(a: TreeNode, b: TreeNode) -> bool:
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


def review2(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    """
    Anki 1-7-24
    Time: 15 min
    """
    def isSameTree(p: TreeNode, q: TreeNode):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        else:
            return False

    if root == None and subRoot:
        return False
    if root.val == subRoot.val:
        if isSameTree(root, subRoot):
            return True
    # d1 else made it return None instead of False
    return review2(root.left, subRoot) or review2(root.right, subRoot)


def review3(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Anki 1-16-24
    Time: 12 min
    """
    def is_same_tree(p: TreeNode, q: TreeNode):
        if p == q == None:
            return True
        elif p and q and p.val == q.val:
            # s2 typo (p.right, p.right)
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        else:
            return False

    def dfs(root: TreeNode, subRoot: TreeNode):
        if root == None:
            return False
        if root.val == subRoot.val:
            same_tree = is_same_tree(root, subRoot)
            if same_tree:
                return True
        # d1 subRoot
        return dfs(root.left, subRoot) or dfs(root.right, subRoot)

    return dfs(root, subRoot)


def review4(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Anki 2-15-24
    """
    def same_tree(r, s):
        if r == s == None:  # s1
            return True  # s1
        if r and s and r.val == s.val:
            return same_tree(r.left, s.left) and same_tree(r.right, s.right)
        else:
            return False

    if not root or not subRoot:  # s2 if not root or subroot
        return False

    if root.val == subRoot.val:
        if same_tree(root, subRoot):
            return True
    return review4(root.left, subRoot) or review4(root.right, subRoot)


def review5(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Mochi 4-20-24
    """
    def same_tree(l: TreeNode, r: TreeNode):
        if not l and not r:
            return True
        if l and r and l.val == r.val:
            return same_tree(l.left, r.left) and same_tree(l.right, r.right)
        return False

    def dfs(root: TreeNode, subRoot: TreeNode):
        if not root:
            return False
        if root.val == subRoot.val:
            if same_tree(root, subRoot):
                return True
        return dfs(root.left, subRoot) or dfs(root.right, subRoot)

    return dfs(root, subRoot)
