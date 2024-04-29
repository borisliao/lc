
import inspect
import pytest
import solution_827


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_827, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
    """
    grid = [[1, 0],
            [0, 1]]
    output = 3

    assert f(grid) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_827, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
    """
    grid = [[1, 1],
            [1, 0]]
    output = 4

    assert f(grid) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_827, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    Explanation: Can't change any 0 to 1, only one island with area = 4.
    """
    grid = [[1, 1],
            [1, 1]]
    output = 4

    assert f(grid) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_827, predicate=inspect.isfunction)])
def test_lc_3(f):
    grid = [[0, 0],
            [0, 0]]
    output = 1

    assert f(grid) == output
