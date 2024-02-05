import inspect
import pytest
import solution_215


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_215, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    output = 5
    assert f(nums, k) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_215, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    output = 4

    assert f(nums, k) == output
