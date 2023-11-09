import pytest
import inspect
import solution_1148


def tn(items: list[int]) -> solution_1148.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> solution_1148.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_1148.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1148, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)

    Explanation:  Nodes in blue are good.

    Root Node (3) is always a good node.

    Node 4 -> (3,4) is the maximum value in the path starting from the root.

    Node 5 -> (3,4,5) is the maximum value in the path

    Node 3 -> (3,1,3) is the maximum value in the path.
    """
    root = tn([3, 1, 4, 3, None, 1, 5])
    output = 4

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1148, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)

    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
    """
    root = tn([3, 3, None, 4, 2])
    output = 3

    assert f(root) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1148, predicate=inspect.isfunction)])
def test_example_3(f):
    """ Explanation: Root is considered as good. """
    root = tn([1])
    output = 1

    assert f(root) == output
