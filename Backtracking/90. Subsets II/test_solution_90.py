import pytest
import inspect
import solution_90


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_90, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 2, 2]
    output = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    assert same_elements(f(nums), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_90, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [0]
    output = [[], [0]]
    assert same_elements(f(nums), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_90, predicate=inspect.isfunction)])
def test_lc_15(f):
    """
    Did you sort the input array `nums`?
    """
    nums = [4, 4, 4, 1, 4]
    output = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [
        1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
    assert same_elements(f(nums), output)
