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


def isBalanced(root: TreeNode) -> bool:
    """
    Solution from neetcode: https://www.youtube.com/watch?v=QfJsau0ItOY
    """
    def dfs(tn: TreeNode):
        if tn is None:
            return {"unbalanced": True, "length": 0}

        left, right = dfs(tn.left), dfs(tn.right)
        weight_difference = abs(left['length'] - right['length'])

        balanced_state = weight_difference <= 1 and left['unbalanced'] and right['unbalanced']
        return {"unbalanced": balanced_state, "length": 1 + max(left['length'], right['length'])}

    return dfs(root)['unbalanced']


def globalVar(root: TreeNode) -> bool:
    """
    Hint from:
     [![@gregoryvan9474](https://yt3.ggpht.com/ytc/AOPolaRUzeM-N91T2Xj8qb5MAoaAveQ1sC_dc1VrUWKt=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/channel/UCXKpafMwrdlABcch9razbtA) 

    ### [@gregoryvan9474](https://www.youtube.com/channel/UCXKpafMwrdlABcch9razbtA)

    [1 year ago (edited)](https://www.youtube.com/watch?v=QfJsau0ItOY&lc=Ugz4wcM_A6q6RPd-Pel4AaABAg)

    I found it makes it a little easier to write the code if you just use a global variable like in the "Diameter of a Binary Tree" problem you solved. Then you can just update the global variable and not have to return two variables in the dfs function.
    """
    unbalanced = False

    def dfs(tn: TreeNode) -> int:
        nonlocal unbalanced
        if unbalanced or tn is None:
            return 0

        left, right = dfs(tn.left), dfs(tn.right)

        if abs(left - right) > 1:
            unbalanced = True

        return 1 + max(left, right)

    dfs(root)
    return True if not unbalanced else False


def review1(root: TreeNode | None) -> bool:
    """
    Anki 12-27-23
    Time: 30 min
    DFS solution
    Used: debugger 2, solution 1
    """
    unbalanced = False

    def dfs(n: TreeNode | None):
        nonlocal unbalanced  # s3
        if unbalanced or n == None:  # s3
            return 0

        left_node = 1 + dfs(n.left)  # d2 1 +
        right_node = 1 + dfs(n.right)  # d2 1 +

        if abs(left_node - right_node) > 1:  # s3
            unbalanced = True  # s3

        return max(left_node, right_node)

    dfs(root)
    return False if unbalanced else True  # s3 unbalanced


def review2(root: TreeNode | None) -> bool:
    """
    Anki 12-28-23
    Time: 8 min
    Used: debugger 1
    """
    state = {"balanced": True}  # d1 flipped state bool

    def dfs(node: TreeNode | None) -> bool:
        if not state['balanced'] or node == None:
            return 0

        l = dfs(node.left)
        r = dfs(node.right)

        if abs(r-l) > 1:
            state['balanced'] = False

        depth = 1 + max(l, r)
        return depth

    dfs(root)
    return state['balanced']


def review3(root: TreeNode | None) -> bool:
    """
    Anki 1-2-24
    Used: debugger 1
    Time: 9 min
    """
    balanced = True

    def dfs(node: TreeNode | None):
        nonlocal balanced  # d1
        if node == None or balanced == False:
            return 0
        left_depth = 1 + dfs(node.left)
        right_depth = 1 + dfs(node.right)

        if abs(left_depth-right_depth) > 1:
            balanced = False

        return max(left_depth, right_depth)

    dfs(root)
    return balanced


def review4(root: TreeNode | None) -> bool:
    """
    Anki 1-22-24
    Time: 16 min
    Used: solution
    """
    balanced = True

    def dfs(root: TreeNode):
        nonlocal balanced
        if not root or not balanced:
            return 0
        left_depth = dfs(root.left)
        right_depth = dfs(root.right)
        if abs(left_depth - right_depth) > 1:
            balanced = False
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return balanced


def review6(root: TreeNode | None) -> bool:
    """
    Anki 1-23-24
    Time: 5 min
    """
    balanced = True

    def dfs(node):
        nonlocal balanced
        if not node or not balanced:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left-right) > 1:
            balanced = False
        return 1 + max(left, right)
    dfs(root)
    return balanced


def review6(root: TreeNode | None) -> bool:
    """
    Anki 1-26-24
    Time: 3:14
    """
    balanced = True

    def dfs(root):
        nonlocal balanced
        if not root or not balanced:
            return 0
        left_depth = dfs(root.left)
        right_depth = dfs(root.right)

        if abs(left_depth-right_depth) > 1:
            balanced = False

        return 1 + max(left_depth, right_depth)

    dfs(root)
    return balanced


def review7(root: TreeNode | None) -> bool:
    """
    Anki 2-6-24
    Time: 4:26
    """
    balanced = True

    def dfs(root):
        nonlocal balanced
        if not balanced or not root:
            return 0
        l = dfs(root.left)
        r = dfs(root.right)
        if abs(l-r) > 1:
            balanced = False
        return 1 + max(l, r)

    dfs(root)
    return balanced


def review8(root: TreeNode | None) -> bool:
    """
    Mochi 4-17-24
    Time: 4:45
    """
    balanced = True

    def dfs(node: TreeNode):
        nonlocal balanced
        if not node or not balanced:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left-right) > 1:
            balanced = False
        return 1+max(left, right)

    dfs(root)
    return balanced
