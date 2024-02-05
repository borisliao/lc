import pytest
import inspect
import solution_23


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_23.ListNode(list[0], ln(list[1:]))
    else:
        return solution_23.ListNode(None)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_23, predicate=inspect.isfunction)])
def test_example_1(f):
    lists = [ln([1, 4, 5]), ln([1, 3, 4]), ln([2, 6])]
    output = ln([1, 1, 2, 3, 4, 4, 5, 6])

    assert str(f(lists)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_23, predicate=inspect.isfunction)])
def test_example_2(f):
    lists = []
    output = None

    assert str(f(lists)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_23, predicate=inspect.isfunction)])
def test_example_3(f):
    lists = [ln([])]
    output = ln([])

    assert str(f(lists)) == str(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_23, predicate=inspect.isfunction)])
def test_lc_13(f):
    lists = [ln([]), ln([-1, 5, 11]), ln([]), ln([6, 10])]
    output = ln([-1, 5, 6, 10, 11])

    assert str(f(lists)) == str(output)
