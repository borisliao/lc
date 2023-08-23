import pytest
import inspect
import solution_3


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "abcabcbb"
    output = 3
    """
    Explanation: The answer is "abc", with the length of 3.
    """

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "bbbbb"
    output = 1
    """
    Explanation: The answer is "b", with the length of 1.
    """

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_example_3(f):
    s = "pwwkew"
    output = 3
    """
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_lc_256(f):
    s = "tmmzuxt"
    output = 5

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_lc_291(f):
    s = "bbtablud"
    output = 6

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_lc_317(f):
    s = "aab"
    output = 2

    assert f(s) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_3, predicate=inspect.isfunction)])
def test_lc_407(f):
    s = "dvdf"
    output = 3

    assert f(s) == output
