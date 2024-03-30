import pytest
import inspect
import solution_84


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_84, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)
    Explanation: The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.
    """
    heights = [2, 1, 5, 6, 2, 3]
    output = 10

    assert f(heights) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_84, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    ![https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)
    """
    heights = [2, 4]
    output = 4

    assert f(heights) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_84, predicate=inspect.isfunction)])
def test_lc_53(f):
    heights = [2, 1, 2]
    output = 3

    assert f(heights) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_84, predicate=inspect.isfunction)])
def test_lc_87(f):
    heights = [1] * 20000
    output = 20000

    assert f(heights) == output
