import pytest
import inspect
import solution_212


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_212, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
    """
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
             ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    output = ["eat", "oath"]

    assert sorted(f(board, words)) == sorted(output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_212, predicate=inspect.isfunction)])
def test_example_2(f):
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    output = []

    assert f(board, words) == output
