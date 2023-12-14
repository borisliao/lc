import pytest
import inspect
import solution_21


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_21.ListNode(list[0], ln(list[1:]))
    else:
        return None


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_21, predicate=inspect.isfunction)])
def test_example_1(f):
    list1 = ln([1, 2, 4])
    list2 = ln([1, 3, 4])
    output = ln([1, 1, 2, 3, 4, 4])

    assert str(f(list1, list2)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_21, predicate=inspect.isfunction)])
def test_example_2(f):
    list1 = ln([])
    list2 = ln([])
    output = ln([])

    assert str(f(list1, list2)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_21, predicate=inspect.isfunction)])
def test_example_3(f):
    list1 = ln([])
    list2 = ln([0])
    output = ln([0])

    assert str(f(list1, list2)) == str(output)
