from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
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


def attempt1(root: TreeNode) -> bool:
    def gn(node: TreeNode, m):
        if not node:
            return 0

        if node.val >= m:
            m = max(m, node.val)
            return 1 + gn(node.left, m) + gn(node.right, m)
        else:
            m = max(m, node.val)
            return 0 + gn(node.left, m) + gn(node.right, m)

    return gn(root, root.val)


def review1(root: TreeNode) -> bool:
    """
    Anki 1-9-24
    Time: 20 min
    """
    def dfs(node: TreeNode | None, largest):
        if node == None:
            return 0

        good_node = 1 if node.val >= largest else 0
        max_largest = max(largest, node.val)

        return good_node + dfs(node.left, max_largest) + dfs(node.right, max_largest)

    return dfs(root, root.val)


def review2(root: TreeNode) -> bool:
    """
    Anki 1-16-24
    Time: 9 min
    """
    def dfs(root: TreeNode, largest: int):
        if not root:
            return 0
        if root.val >= largest:
            return 1 + dfs(root.left, max(root.val, largest)) + dfs(root.right, max(root.val, largest))
        else:
            return dfs(root.left, largest) + dfs(root.right, largest)

    return dfs(root, root.val)

# def review3(root: TreeNode) -> bool:
#     """
#     Anki 1-16-24
#     Time:
#     """
