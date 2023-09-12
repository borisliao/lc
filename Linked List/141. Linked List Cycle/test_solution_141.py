import pytest
import inspect
import solution_141


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_141.ListNode(list[0], ln(list[1:]))
    else:
        return None


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_141, predicate=inspect.isfunction)])
def test_example_1(f):
    """![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)"""
    head = ln([3, 2, 0, -4])
    head.next.next.next = head.next
    output = True
    """Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed)."""

    assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_141, predicate=inspect.isfunction)])
def test_example_2(f):
    """![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)"""
    head = ln([1, 2])
    head.next = head
    output = True
    """Explanation: There is a cycle in the linked list, where the tail connects to the 0th node."""

    assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_141, predicate=inspect.isfunction)])
def test_example_3(f):
    """![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)"""
    head = ln([1])
    output = False

    assert str(f(head)) == str(output)
