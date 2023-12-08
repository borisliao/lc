import pytest
import inspect
import solution_79


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_example_1(f):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    output = True

    assert f(board, word) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_example_2(f):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    output = True

    assert f(board, word) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_example_3(f):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    output = False

    assert f(board, word) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_lc_11(f):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    output = False

    assert f(board, word) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_lc_13(f):
    board = [["a", "a"]]
    word = "aaa"
    output = False

    assert f(board, word) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_79, predicate=inspect.isfunction)])
def test_lc_31(f):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    output = True

    assert f(board, word) == output
