import pytest
import inspect
import solution_143


def ln(list):
    """From a list, builds a ListNode data structure"""
    if (list):
        return solution_143.ListNode(list[0], ln(list[1:]))
    else:
        return None

@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_143, predicate=inspect.isfunction)])
def test_example_1(f):
    head = ln([1, 2, 3, 4])
    output = ln([1, 4, 2, 3])

    f(head)
    assert str(head) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_143, predicate=inspect.isfunction)])
def test_example_2(f):
    head = ln([1, 2, 3, 4, 5])
    output = ln([1, 5, 2, 4, 3])

    f(head)
    assert str(head) == str(output)
