import pytest
import inspect
import solution_153


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_153, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [3, 4, 5, 1, 2]
    output = 1
    """
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
    """

    assert f(nums) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_153, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [4, 5, 6, 7, 0, 1, 2]
    output = 0
    """
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
    """

    assert f(nums) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_153, predicate=inspect.isfunction)])
def test_lc_3(f):
    nums = [1]
    output = 1

    assert f(nums) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_153, predicate=inspect.isfunction)])
def test_lc_3(f):
    nums = [2, 1]
    output = 1

    assert f(nums) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_153, predicate=inspect.isfunction)])
def test_lc_11(f):
    nums = [11, 13, 15, 17]
    output = 11
    """
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
    """

    assert f(nums) == output
