import pytest
import inspect
import solution_347


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_347, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = [1, 2]

    assert f(nums, k) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_347, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [1]
    k = 1
    output = [1]

    assert f(nums, k) == output
