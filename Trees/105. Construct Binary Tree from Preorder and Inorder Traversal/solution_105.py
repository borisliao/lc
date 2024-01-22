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


def review2(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-21-24
    """
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)
    root.left = review2(preorder[1:mid+1], inorder[:mid])
    root.right = review2(preorder[mid+1:], inorder[mid+1:])
    return root


def review3(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-21-24
    Time: 5 min
    Used: solution 1
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    distance_to_mid = inorder.index(root.val)
    root.left = review3(preorder[1: distance_to_mid+1],
                        inorder[:distance_to_mid+1])
    root.right = review3(
        preorder[distance_to_mid+1:], inorder[distance_to_mid+1:])  # s1 +1

    return root


def review4(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-21-24
    Time: 4 min
    """
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    m = inorder.index(preorder[0])
    root.left = review4(preorder[1:m+1], inorder[:m])
    root.right = review4(preorder[m+1:], inorder[m+1:])
    return root

# def review5(preorder: list[int], inorder: list[int]) -> TreeNode:
#     """
#     Anki 1-21-24
#     Time: 4 min
#     Used: https://www.youtube.com/watch?v=ihj4IQGZ2zc
#     """
