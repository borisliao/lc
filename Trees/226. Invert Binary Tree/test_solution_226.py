import pytest
import inspect
import solution_226


def tn(items: list[int]) -> solution_226.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_226.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_226.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_226, predicate=inspect.isfunction)])
def test_example_1(f):
    """![https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)"""
    root = tn([4, 2, 7, 1, 3, 6, 9])
    output = tn([4, 7, 2, 9, 6, 3, 1])

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_226, predicate=inspect.isfunction)])
def test_example_2(f):
    """![https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)"""
    root = tn([2, 1, 3])
    output = tn([2, 3, 1])

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_226, predicate=inspect.isfunction)])
def test_example_3(f):
    root = tn([])
    output = tn([])

    assert f(root) == output
