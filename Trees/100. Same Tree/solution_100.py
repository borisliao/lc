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


def attempt1(p: TreeNode, q: TreeNode) -> bool:
    """Recrusive dfs"""
    same_values = True
    p_left = p.left if p and p.left else None
    q_left = q.left if q and q.left else None
    if p_left or q_left:
        if attempt1(p_left, q_left) is False:
            same_values = False

    p_right = p.right if p and p.right else None
    q_right = q.right if q and q.right else None
    if p_right or q_right:
        if attempt1(p_right, q_right) is False:
            same_values = False

    if not (same_values and (p == q or (p != None and q != None) and (p.val == q.val))):
        same_values = False

    return same_values


def leetCode_572(p: TreeNode, q: TreeNode) -> bool:
    """
    This solution comes from neetcode, from problem 572
    https://www.youtube.com/watch?v=E36O5SWp-LE
    """
    if p == None and q == None:
        return True
    if p and q and (p.val == q.val):
        return (leetCode_572(p.left, q.left) and leetCode_572(p.right, q.right))
    return False


# def attempt2(p: TreeNode, q: TreeNode) -> bool:
#     """itterative bfs"""
#     pq: Deque['TreeNode'] = deque()
#     qq: Deque['TreeNode'] = deque()

#     pq.append(p)
#     qq.append(q)

#     while pq and qq:
#         p_res, q_res = pq.pop(), qq.pop()

#         if not p and not q:
#             return True
#         if p_res.val != q_res.val:
#             return False
#         if p_res.left:
#             pq.append(p_res.left)
#         if p_res.right:
#             pq.append(p_res.right)
#         if q_res.left:
#             qq.append(q_res.left)
#         if q_res.right:
#             qq.append(q_res.right)

#     return True

# def solution_lc_BFS(p: TreeNode, q: TreeNode) -> bool:
#     """
#     itterative bfs
#     https://leetcode.com/problems/same-tree/solutions/361737/python3-recursively-and-bfs-and-dfs-iteratively/
#     """
#     pq: Deque['TreeNode'] = deque()
#     qq: Deque['TreeNode'] = deque()

#     while pq and qq:
#         p, q = pq.popleft(), qq.popleft()
#         if not p and not q:
#             continue
#         elif (not p or not q) or (p.val != q.val):
#             return False
#         pq.append(p.left)
#         pq.append(p.right)
#         qq.append(q.left)
#         qq.append(q.right)

#     return True

def review1(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Anki 12-23-23
    Time: 10 min
    """
    def dfs(p: TreeNode | None, q: TreeNode | None):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        else:
            return False

    return dfs(p, q)


def review2(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Anki 12-23-23
    Time: 15 min
    Used: solution
    """
    def dfs(p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return False

    return dfs(p, q)


def review3(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Anki 12-28-23
    Used: Debugger 1
    """
    def dfs(p, q):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:  # d1 p.vap
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        else:
            return False

    return dfs(p, q)


# def review3(p: TreeNode | None, q: TreeNode | None) -> bool:
#     """
#     Anki 12-31-23
#     Did not whiteboard, and got overengineered solution
#     """
#     same_tree = True

#     def dfs(p, q):
#         nonlocal same_tree
#         if not same_tree or p and q and p.val != q.val:
#             same_tree = False
#             return False

#         if p == None and q == None:
#             return True

#         if p and q and p.val == q.val:
#             return dfs(p.left, q.left) and dfs(p.right, q.right)

#     dfs(p, q)
#     return same_tree


def review4(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Anki 12-31-23
    Time: 11 min
    Used: Solution 2
    Note: Whiteboard the solution first.
    """

    def dfs(p, q):
        if p == None and q == None:
            return True

        if p and q and p.val == q.val:  # s1 p.val != q.val
            return dfs(p.left, q.left) and dfs(p.right, q.right)  # d1
        else:
            return False  # s1 return false if p or q doesnt exist

    return dfs(p, q)


def review5(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Anki 1-17-24
    Time: 2 min
    """
    if p == None and q == None:
        return True
    elif p and q and p.val == q.val:
        return review5(p.left, q.left) and review5(p.right, q.right)
    else:
        return False


def review6(p: TreeNode, q: TreeNode) -> bool:
    """
    Mochi 4-16-24
    """
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return review6(p.left, q.left) and review6(p.right, q.right)
    return False
