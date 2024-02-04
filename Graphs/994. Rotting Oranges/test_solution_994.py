
import inspect
import pytest
import solution_994


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_994, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2019/02/16/oranges.png](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)
    """
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    output = 4
    assert f(grid) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_994, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    """
    grid = [[2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]]
    output = -1

    assert f(grid) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f",
                         [f[1] for f in inspect.getmembers(solution_994, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
    """
    grid = [[0, 2]]
    output = 0

    assert f(grid) == output
