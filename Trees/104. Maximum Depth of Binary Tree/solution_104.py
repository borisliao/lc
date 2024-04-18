# Definition for a binary tree node.
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


def maxDepth(root: TreeNode) -> int:
    """attempt 1, DFS, recursive"""
    if root:
        left_depth = 1 + maxDepth(root.left)
        right_depth = 1 + maxDepth(root.right)

        return max(left_depth, right_depth)

    return 0


def BFS(root: TreeNode) -> int:
    """attempt 2, BFS, recursive, no queue (using lists)"""
    if not root:
        return 0

    left_nodes: list[TreeNode] = []
    right_nodes: list[TreeNode] = []
    if root.left:
        left_nodes.append(root.left)
    if root.right:
        right_nodes.append(root.right)

    count = 1
    while left_nodes or right_nodes:
        new_left = []
        for node in left_nodes:
            if node.left:
                new_left.append(node.left)
            if node.right:
                new_left.append(node.right)
        left_nodes = new_left

        new_right = []
        for node in right_nodes:
            if node.left:
                new_right.append(node.left)
            if node.right:
                new_right.append(node.right)
        right_nodes = new_right
        count += 1

    return count


def review1(root: TreeNode | None) -> int:
    """
    Anki 12-26-23
    Time: 25:31
    Used: debugger 2
    """
    level = 0
    nodes = [root] if root else None  # d2

    while nodes:
        level += 1
        new_nodes = []
        for n in nodes:  # d1
            if n.left:
                new_nodes.append(n.left)
            if n.right:
                new_nodes.append(n.right)
        nodes = new_nodes

    return level


def review2(root: TreeNode | None) -> int:
    """
    Anki 12-27-23
    Time: 3 min
    Used: solution 1
    """
    if root == None:
        return 0
    left_depth = 1 + review2(root.left)
    right_depth = 1 + review2(root.right)

    return max(left_depth, right_depth)  # s1


def review3(root: TreeNode | None) -> int:
    """
    Anki 12-27-23
    Itterative solution
    Used: [Maximum Depth of Binary Tree - 3 Solutions - Leetcode 104 - Python](https://www.youtube.com/watch?v=hTM3phVI6YQ)
    Time: 9:27
    """
    stack: list[list[TreeNode, int] | list] = [[root, 1]] if root else []

    max_depth = 0
    while stack:
        n, depth = stack.pop()

        if not n:
            max_depth = max(max_depth, depth-1)
            continue

        stack.append([n.left, depth + 1])
        stack.append([n.right, depth + 1])
    return max_depth


def review4(root: TreeNode | None) -> int:
    """
    Anki 12-31-23
    Time: 4 min
    """
    def dfs(node):
        if node == None:
            return 0
        return 1 + max(dfs(node.left), dfs(node.right))

    return dfs(root)


def review5(root: TreeNode | None) -> int:
    """
    Mochi 4-18-24
    """
    levels = 0
    q = [root] if root else []

    while q:
        levels += 1
        new_q = []

        for n in q:
            if n.left:
                new_q.append(n.left)
            if n.right:
                new_q.append(n.right)
        q = new_q

    return levels
