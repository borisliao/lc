import pytest
import inspect
import solution_46


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_46, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 2, 3]
    output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    assert same_elements(f(nums), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_46, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [0, 1]
    output = [[0, 1], [1, 0]]
    assert same_elements(f(nums), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_46, predicate=inspect.isfunction)])
def test_example_3(f):
    nums = [1]
    output = [[1]]

    assert same_elements(f(nums), output)
