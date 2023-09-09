import pytest
import inspect
import solution_19


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_19.ListNode(list[0], ln(list[1:]))
    else:
        return None


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_19, predicate=inspect.isfunction)])
def test_example_1(f):
    head = ln([1, 2, 3, 4, 5])
    n = 2
    output = ln([1, 2, 3, 5])

    assert str(f(head, n)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_19, predicate=inspect.isfunction)])
def test_example_2(f):
    head = [1]
    n = 1
    output = ln([])

    assert str(f(head, n)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_19, predicate=inspect.isfunction)])
def test_example_3(f):
    head = [1, 2]
    n = 1
    output = ln([1])

    assert str(f(head, n)) == str(output)
