import pytest
import inspect
import solution_121


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_121, predicate=inspect.isfunction)])
def test_example_1(f):
    prices = [7, 1, 5, 3, 6, 4]
    output = 5
    """
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    """

    assert f(prices) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_121, predicate=inspect.isfunction)])
def test_example_2(f):
    prices = [7, 6, 4, 3, 1]
    output = 0
    """
    Explanation: In this case, no transactions are done and the max profit = 0.
    """

    assert f(prices) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_121, predicate=inspect.isfunction)])
def test_lc_154(f):
    prices = [2, 4, 1]
    output = 2

    assert f(prices) == output
