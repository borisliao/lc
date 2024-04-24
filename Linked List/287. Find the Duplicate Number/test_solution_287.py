import pytest
import inspect
import solution_287


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_287, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 3, 4, 2, 2]
    output = 2

    assert str(f(nums)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_287, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [3, 1, 3, 4, 2]
    output = 3

    assert str(f(nums)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_287, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [3, 3, 3, 3, 3]
    output = 3

    assert str(f(nums)) == str(output)
