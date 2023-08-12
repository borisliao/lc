import pytest
import inspect
import solution_217


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_217, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 2, 3, 1]
    output = True

    assert f(nums) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_217, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [1, 2, 3, 4]
    output = False

    assert f(nums) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_217, predicate=inspect.isfunction)])
def test_example_3(f):
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output = True

    assert f(nums) == output
