import pytest
import inspect
import solution_297


def tn(items: list[int]) -> solution_297.TreeNode:
    """
    From a list of values, create a TreeNode
    Source: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
    """
    n = len(items)
    if n == 0:
        return solution_297.TreeNode(None)

    def inner(index: int = 0) -> solution_297.TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = solution_297.TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_297, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
    """
    root = tn([1, 2, 3, None, None, 4, 5])
    output = tn([1, 2, 3, None, None, 4, 5])

    ser = f()
    deser = f()

    assert str(deser.deserialize(ser.serialize(root))) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_297, predicate=inspect.isfunction)])
def test_example_2(f):
    root = tn([])
    output = tn([])

    ser = f()
    deser = f()

    assert str(deser.deserialize(ser.serialize(root))) == str(output)
