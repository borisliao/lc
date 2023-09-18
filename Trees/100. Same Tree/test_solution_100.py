import pytest
import inspect
import solution_100


def tn(items: list[int]) -> solution_100.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_100.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_100.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_100, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)
    """
    p = tn([1, 2, 3])
    q = tn([1, 2, 3])
    output = True

    assert f(p, q) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_100, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
    """
    p = tn([1, 2])
    q = tn([1, None, 2])
    output = False

    assert f(p, q) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_100, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    ![https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
    """
    p = tn([1, 2, 1])
    q = tn([1, 1, 2])
    output = False

    assert f(p, q) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_100, predicate=inspect.isfunction)])
def test_lc_19(f):
    p = tn([5, None, 5, None, -3])
    q = tn([5, -3, None, 9])
    output = False

    assert f(p, q) == output
