import pytest
import inspect
import solution_680


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_680, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "aba"
    output = True

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_680, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "abca"
    output = True

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_680, predicate=inspect.isfunction)])
def test_example_3(f):
    s = "abc"
    output = False

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_680, predicate=inspect.isfunction)])
def test_lc_384(f):
    """
    Make sure function only deletes one character
    """
    s = "eeccccbebaeeabebccceea"
    output = False

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_680, predicate=inspect.isfunction)])
def test_lc_466(f):
    """
    Check if it removed the 6th character 'e' instead of the 16th character 'c'
    "ebcbbececabbacecbbcbe"
          ^         ^
         6th       16th
    """
    s = "ebcbbececabbacecbbcbe"
    output = True

    assert f(s) == output
