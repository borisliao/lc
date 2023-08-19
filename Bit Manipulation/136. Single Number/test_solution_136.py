import pytest
import inspect
import solution_136


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_136, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [2, 2, 1]
    output = 1
    assert f(nums) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_136, predicate=inspect.isfunction)])
def test_example_2(f):

    nums = [4, 1, 2, 1, 2]
    output = 4

    assert f(nums) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_136, predicate=inspect.isfunction)])
def test_example_3(f):
    nums = [1]
    output = 1

    assert f(nums) == output
