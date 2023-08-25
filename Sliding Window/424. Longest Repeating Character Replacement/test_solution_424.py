import pytest
import inspect
import solution_424


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_424, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "ABAB"
    k = 2
    output = 4
    """
    Explanation: Replace the two 'A's with two 'B's or vice versa.
    """

    assert f(s, k) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_424, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "AABABBA"
    k = 1
    output = 4
    """
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achive this answer too.
    """

    assert f(s, k) == output
