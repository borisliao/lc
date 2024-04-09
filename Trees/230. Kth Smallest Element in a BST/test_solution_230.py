import pytest
import inspect
import solution_230


def tn(items: list[int]) -> solution_230.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_230.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_230.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_230, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
    """
    root = tn([3, 1, 4, None, 2])
    k = 1
    output = 1

    assert f(root, k) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_230, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
    """
    root = tn([5, 3, 6, 2, 4, None, None, 1])
    k = 3
    output = 3

    assert f(root, k) == output
