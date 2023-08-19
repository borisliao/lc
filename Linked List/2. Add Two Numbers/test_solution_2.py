import pytest
import inspect
import solution_2


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_2.ListNode(list[0], ln(list[1:]))
    else:
        return None


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_2, predicate=inspect.isfunction)])
def test_example_1(f):

    l1 = ln([2, 4, 3])
    l2 = ln([5, 6, 4])
    output = ln([7, 0, 8])

    assert str(f(l1, l2)) == str(output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_2, predicate=inspect.isfunction)])
def test_example_2(f):
    l1 = ln([0])
    l2 = ln([0])
    output = ln([0])

    assert str(f(l1, l2)) == str(output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_2, predicate=inspect.isfunction)])
def test_example_3(f):
    l1 = ln([9, 9, 9, 9, 9, 9, 9])
    l2 = ln([9, 9, 9, 9])
    output = ln([8, 9, 9, 9, 0, 0, 0, 1])

    assert str(f(l1, l2)) == str(output)
