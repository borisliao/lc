import pytest
import inspect
import solution_98


def tn(items: list[int]) -> solution_98.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_98.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_98.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_98, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
    """
    root = tn([2, 1, 3])
    output = True

    assert f(root) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_98, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

    Explanation: The root node's value is 5 but its right child's value is 4.
    """
    root = tn([5, 1, 4, None, None, 3, 6])
    output = False

    assert f(root) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_98, predicate=inspect.isfunction)])
def test_lc_76(f):
    root = tn([5, 4, 6, None, None, 3, 7])
    output = False

    assert f(root) == output
