import pytest
import inspect
import solution_51


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_51, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2020/11/13/queens.jpg](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    """
    n = 4
    output = [[".Q..", "...Q", "Q...", "..Q."],
              ["..Q.", "Q...", "...Q", ".Q.."]]

    assert f(n) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_51, predicate=inspect.isfunction)])
def test_example_2(f):
    n = 1
    output = [["Q"]]

    assert f(n) == output
