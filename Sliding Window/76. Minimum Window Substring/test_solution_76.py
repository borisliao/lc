import pytest
import inspect
import solution_76


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_76, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "ADOBECODEBANC"
    t = "ABC"
    output = "BANC"
    """
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    """

    assert f(s, t) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_76, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "a"
    t = "a"
    output = "a"
    """
    Explanation: The entire string s is the minimum window.
    """

    assert f(s, t) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_76, predicate=inspect.isfunction)])
def test_example_3(f):
    s = "a"
    t = "aa"
    output = ""
    """
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
    """

    assert f(s, t) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_76, predicate=inspect.isfunction)])
def test_lc_136(f):
    s = "aa"
    t = "aa"
    output = "aa"

    assert f(s, t) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_76, predicate=inspect.isfunction)])
def test_lc_196(f):
    s = "bba"
    t = "ab"
    output = "ba"

    assert f(s, t) == output
