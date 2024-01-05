import pytest
import inspect
import solution_150


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_150, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: ((2 + 1) \* 3) = 9
    """
    tokens = ["2", "1", "+", "3", "*"]
    output = 9

    assert f(tokens) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_150, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: (4 + (13 / 5)) = 6
    """
    tokens = ["4", "13", "5", "/", "+"]
    output = 6

    assert f(tokens) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_150, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    output = 22

    assert f(tokens) == output
