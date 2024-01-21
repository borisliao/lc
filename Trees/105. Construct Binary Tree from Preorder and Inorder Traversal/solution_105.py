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


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root


def review1(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-21-24
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = review1(preorder[1:mid+1], inorder[:mid])
    root.right = review1(preorder[mid+1:], inorder[mid+1:])
    return root


# def review2(preorder: list[int], inorder: list[int]) -> TreeNode:
#     """
#     Anki 1-21-24
#     """
