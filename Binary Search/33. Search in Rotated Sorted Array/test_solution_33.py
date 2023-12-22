import pytest
import inspect
import solution_33


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_33, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    output = 4

    assert f(nums, target) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_33, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    output = -1

    assert f(nums, target) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_33, predicate=inspect.isfunction)])
def test_example_3(f):
    nums = [1]
    target = 0
    output = -1

    assert f(nums, target) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_33, predicate=inspect.isfunction)])
def test_lc_192(f):
    nums = [3, 1]
    target = 1
    output = 1

    assert f(nums, target) == output
