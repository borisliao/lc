import pytest
import inspect
import solution_102


def tn(items: list[int]) -> solution_102.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_102.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_102.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_102, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2021/02/14/tree.jpg](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)    """
    root = tn([1, 2, 3, None, 5, None, 4])
    output = [1, 3, 4]

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_102, predicate=inspect.isfunction)])
def test_example_2(f):
    root = tn([1, None, 3])
    output = [1, 3]

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_102, predicate=inspect.isfunction)])
def test_lc_166(f):
    root = tn([])
    output = []

    assert f(root) == output
