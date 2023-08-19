import pytest
import inspect
import solution_242


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_242, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "anagram"
    t = "nagaram"
    output = True

    assert f(s=s, t=t) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_242, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "rat"
    t = "car"
    output = False

    assert f(s=s, t=t) == output

# LC test cases


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_242, predicate=inspect.isfunction)])
def test_lc_34(f):
    s = "aacc"
    t = "ccac"
    output = False

    assert f(s=s, t=t) == output
