import pytest
import inspect
import solution_81


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_81, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    output = True

    assert f(nums, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_81, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    output = False

    assert f(nums, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_81, predicate=inspect.isfunction)])
def test_lc_2(f):
    nums = [1]
    target = 0
    output = False

    assert f(nums, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_81, predicate=inspect.isfunction)])
def test_lc_215(f):
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    target = 2
    output = True

    assert f(nums, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_81, predicate=inspect.isfunction)])
def test_lc_233(f):
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 13
    output = True

    assert f(nums, target) == output
