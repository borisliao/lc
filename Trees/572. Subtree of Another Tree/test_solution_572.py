import pytest
import inspect
import solution_572


def tn(items: list[int]) -> solution_572.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_572.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_572.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_572, predicate=inspect.isfunction)])
def test_example_1(f):
    """![https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)"""
    root = tn([3, 4, 5, 1, 2])
    subRoot = tn([4, 1, 2])
    output = True

    assert f(root, subRoot) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_572, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
    """
    root = tn([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = tn([4, 1, 2])
    output = False

    assert f(root, subRoot) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_572, predicate=inspect.isfunction)])
def test_lc_166(f):
    """
    ![https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
    """
    root = tn([1, 1])
    subRoot = tn([1])
    output = True

    assert f(root, subRoot) == output
