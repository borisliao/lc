import pytest
import inspect
import solution_235


def tn(items: list[int]) -> solution_235.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_235.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_235.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_235, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
    """
    root = tn([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # 2
    q = root.right  # 8
    output = 6
    """Explanation: The LCA of nodes 2 and 8 is 6."""

    assert f(root, p, q).val == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_235, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
    """
    root = tn([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # 2
    q = root.left.right  # 4
    output = 2
    """Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition."""

    assert f(root, p, q).val == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_235, predicate=inspect.isfunction)])
def test_lc_166(f):
    """
    ![https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
    """
    root = tn([2, 1])
    p = root  # 2
    q = root.left  # 1
    output = 2

    assert f(root, p, q).val == output
