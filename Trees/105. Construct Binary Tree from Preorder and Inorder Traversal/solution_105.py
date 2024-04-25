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


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
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


def review5(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-26-24
    Time: 30 min
    Used: https://www.youtube.com/watch?v=ihj4IQGZ2zc, solution 2, debugger 1
    """
    if not preorder or not inorder:  # s3 or not inorder
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])  # s2 [1]
    # d1 TreeNode(inorder[mid-1])
    root.left = review5(preorder[1: mid + 1], inorder[:mid])
    root.right = review5(preorder[mid+1:], inorder[mid+1:])  # d1 +1
    return root


def review6(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-26-24
    Time: 10 min
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    left_tree = mid
    root.left = review6(preorder[1:left_tree+1], inorder[:mid])
    root.right = review6(preorder[left_tree+1:], inorder[mid+1:])

    return root


def review7(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 1-28-24
    Time: 8 min
    Whiteboard the proof with complex example
    """
    if not preorder or not inorder:  # s1
        return None  # s1
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    left_tree = mid
    root.left = review7(preorder[1:left_tree+1], inorder[:mid])
    root.right = review7(preorder[left_tree+1:], inorder[mid+1:])
    return root


def review8(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 2-3-24
    Whiteboard the proof with complex example
    Used: Debugger 4
    Time: 13 min
    """
    if not preorder or not inorder:  # d2, d3 if not root, d4 not preorder or not inorder
        return None  # d2
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    left_nodes = mid  # 1
    # preorder 1 2 3 4 5
    # inorder  2 1 3 4 5
    root.left = review8(preorder[1:left_nodes+1], inorder[:mid])
    root.right = review8(preorder[left_nodes+1:],
                         inorder[mid+1:])  # d1 inorder[mid+1]
    return root


def review9(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 2-13-24
    """
    if not preorder or not inorder:  # s2
        return None  # s2
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])  # s1 preorder[1]
    left_nodes = mid
    root.left = review9(preorder[1:left_nodes+1], inorder[:mid])
    root.right = review9(preorder[left_nodes+1:], inorder[mid+1:])
    return root


def review10(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Anki 2-13-24
    """
    if not inorder or not preorder:  # s1 or preorder
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    left_tree = mid
    root.left = review10(preorder[1:left_tree+1], inorder[:mid])
    root.right = review10(preorder[left_tree+1:], inorder[mid+1:])
    return root


def review11(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Mochi 4-15-24
    """
    if not inorder or not preorder:  # s1
        return None  # s1
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])  # s1 preorder.index(inorder
    root.left = review11(preorder[1:mid+1], inorder[:mid])
    root.right = review11(preorder[mid+1:], inorder[mid+1:])
    return root


def review12(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Mochi 4-24-24
    """
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)
    root.left = review12(preorder[1:mid+1], inorder[:mid])
    root.right = review12(preorder[mid+1:], inorder[mid+1:])
    return root
