import pytest
import inspect
import solution_704


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_704, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    output = 4
    """
    Explanation: 9 exists in nums and its index is 4
    """

    assert f(nums, target) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_704, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    output = -1
    """
    Explanation: 2 does not exist in nums so return -1
    """

    assert f(nums, target) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_704, predicate=inspect.isfunction)])
def test_lc_11(f):
    nums = [2, 5]
    target = 2
    output = 0

    assert f(nums, target) == output
