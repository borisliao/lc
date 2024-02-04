
import inspect
import pytest
import solution_130


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_130, predicate=inspect.isfunction)])
def test_example_1(f):
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    output = [["X", "X", "X", "X"],
              ["X", "X", "X", "X"],
              ["X", "X", "X", "X"],
              ["X", "O", "X", "X"]]

    assert f(board) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_130, predicate=inspect.isfunction)])
def test_example_2(f):
    board = [["X"]]
    output = [["X"]]

    assert f(board) == output
