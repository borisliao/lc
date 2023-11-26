import pytest
import inspect
import solution_105


def tn(items: list[int]) -> solution_105.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_105.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_105.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_105, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2021/02/19/tree.jpg](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
    """
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    output = tn([3, 9, 20, None, None, 15, 7])

    assert f(preorder, inorder) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_105, predicate=inspect.isfunction)])
def test_example_2(f):
    preorder = [-1]
    inorder = [-1]
    output = tn([-1])

    assert f(preorder, inorder) == output
