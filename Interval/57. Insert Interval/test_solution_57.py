import pytest
import inspect
import solution_57


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_57, predicate=inspect.isfunction)])
def test_example_1(f):
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    output = [[1, 5], [6, 9]]

    assert f(intervals, newInterval) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_57, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    """
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    output = [[1, 2], [3, 10], [12, 16]]

    assert f(intervals, newInterval) == output
