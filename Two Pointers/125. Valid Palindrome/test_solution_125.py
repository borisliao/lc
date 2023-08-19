import pytest
import inspect
import solution_125


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_125, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "A man, a plan, a canal: Panama"
    output = True

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_125, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "race a car"
    output = False

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_125, predicate=inspect.isfunction)])
def test_example_3(f):
    s = " "
    output = True

    assert f(s) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_125, predicate=inspect.isfunction)])
def test_lc_462(f):
    s = "0P"
    output = False

    assert f(s) == output
