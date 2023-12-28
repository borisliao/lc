import pytest
import inspect
import solution_110


def tn(items: list[int]) -> solution_110.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_110.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_110.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_110, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)
    """
    root = tn([3, 9, 20, None, None, 15, 7])
    output = True

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_110, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)
    """
    root = tn([1, 2, 2, 3, 3, None, None, 4, 4])
    output = False

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_110, predicate=inspect.isfunction)])
def test_example_3(f):
    root = tn([])
    output = True

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_110, predicate=inspect.isfunction)])
def test_lc_203(f):
    root = tn([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    output = False

    assert f(root) == output
