import pytest
import inspect
import solution_25


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_25.ListNode(list[0], ln(list[1:]))
    else:
        return solution_25.ListNode(None)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_25, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
    """
    head = ln([1, 2, 3, 4, 5])
    k = 2
    output = ln([2, 1, 4, 3, 5])

    assert str(f(head, k)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_25, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)
    """
    head = [1, 2, 3, 4, 5]
    k = 3
    output = [3, 2, 1, 4, 5]

    assert str(f(head, k)) == str(output)
