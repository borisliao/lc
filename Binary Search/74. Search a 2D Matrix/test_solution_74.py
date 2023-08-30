import pytest
import inspect
import solution_74


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_74, predicate=inspect.isfunction)])
def test_example_1(f):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    output = True

    assert f(matrix, target) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_74, predicate=inspect.isfunction)])
def test_example_2(f):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    output = False

    assert f(matrix, target) == output
