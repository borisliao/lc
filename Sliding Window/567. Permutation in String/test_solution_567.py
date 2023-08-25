import pytest
import inspect
import solution_567


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_567, predicate=inspect.isfunction)])
def test_example_1(f):
    s1 = "ab"
    s2 = "eidbaooo"
    output = True
    """
    Explanation: s2 contains one permutation of s1 ("ba").
    """

    assert f(s1, s2) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_567, predicate=inspect.isfunction)])
def test_example_2(f):
    s1 = "ab"
    s2 = "eidboaoo"
    output = False

    assert f(s1, s2) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_567, predicate=inspect.isfunction)])
def test_lc_90(f):
    s1 = "hello"
    s2 = "ooolleoooleh"
    output = False

    assert f(s1, s2) == output
