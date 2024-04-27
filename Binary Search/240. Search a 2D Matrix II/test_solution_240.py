import pytest
import inspect
import solution_240


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_240, predicate=inspect.isfunction)])
def test_example_1(f):
    """![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)"""
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    output = True

    assert f(matrix, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_240, predicate=inspect.isfunction)])
def test_example_2(f):
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    output = False

    assert f(matrix, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_240, predicate=inspect.isfunction)])
def test_lc_78(f):
    """
    Tests if it can check matrix of len 1
    """
    matrix = [[-5]]
    target = -5
    output = True

    assert f(matrix, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_240, predicate=inspect.isfunction)])
def test_lc_111(f):
    """
    Tests if you can check a martix of len 2
    """
    matrix = [[-1, 3]]
    target = 3
    output = True

    assert f(matrix, target) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_240, predicate=inspect.isfunction)])
def test_lc_124(f):
    matrix = [[1], [3], [5]]
    target = 3
    output = True

    assert f(matrix, target) == output
