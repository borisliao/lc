import pytest
import inspect
import solution_206


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_206.ListNode(list[0], ln(list[1:]))
    else:
        return None


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_206, predicate=inspect.isfunction)])
def test_example_1(f):
    head = ln([1, 2, 3, 4, 5])
    output = ln([5, 4, 3, 2, 1])

    assert str(f(head)) == str(output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_206, predicate=inspect.isfunction)])
def test_example_2(f):
    head = ln([1, 2])
    output = ln([2, 1])

    assert str(f(head)) == str(output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_206, predicate=inspect.isfunction)])
def test_example_3(f):
    head = ln([])
    output = ln([])

    assert str(f(head)) == str(output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_206, predicate=inspect.isfunction)])
def test_lc_25(f):
    head = ln([0, 1, 4, -2])
    output = ln([-2, 4, 1, 0])

    assert str(f(head)) == str(output)
