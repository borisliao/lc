from collections import deque


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


def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    level_nodes = [root]
    node_values = []
    while level_nodes:
        new_level_nodes = []
        new_node_values = []
        for node in level_nodes:
            new_node_values.append(node.val)
            if node.left:
                new_level_nodes.append(node.left)
            if node.right:
                new_level_nodes.append(node.right)
        level_nodes = new_level_nodes
        node_values.append(new_node_values)

    return node_values


def review1(root: TreeNode | None) -> list[list[int]]:
    """
    Anki 12-24-23
    Time: 18 min
    Used: Debugger 2
    """
    result = []
    stack: deque[TreeNode] = deque()  # d2 used deque for o(n) pop

    if root:
        stack.append(root)

    while stack:
        layer = []
        for _ in range(len(stack)):
            value = stack.popleft()  # d2 used deque for o(n) pop
            # d1 value instead of value.val (did not read question)
            layer.append(value.val)
            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)

        result.append(layer)

    return result


def review2(root: TreeNode | None) -> list[list[int]]:
    """
    Anki 12-31-23
    Time: 15 min
    Used: debugger 1
    """
    stack = [root] if root else []
    result = []  # d1 redundent [root.val] in init

    while stack:
        n_stack = []
        n_result = []

        for n in stack:
            if n.left:
                n_stack.append(n.left)
            if n.right:
                n_stack.append(n.right)
            n_result.append(n.val)

        result.append(n_result)
        stack = n_stack

    return result


def review3(root: TreeNode | None) -> list[list[int]]:
    """
    Anki 1-16-24
    """
    level = [root] if root else []
    result = []

    while level:
        level_values = []
        new_level = []
        for n in level:
            level_values.append(n.val)
            if n.left:
                new_level.append(n.left)
            if n.right:
                new_level.append(n.right)
        result.append(level_values)
        level = new_level

    return result


def review4(root: TreeNode | None) -> list[list[int]]:
    """
    Mochi 4-17-24
    """
    result = []
    subset = []
    q: list[TreeNode] = [root] if root else []  # d1 []
    while q:
        new_q = []
        for node in q:
            subset.append(node.val)
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        result.append(subset.copy())
        subset = []
        q = new_q

    return result
