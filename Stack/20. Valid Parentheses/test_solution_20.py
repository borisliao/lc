import pytest
import inspect
import solution_20


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_20, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "()"
    output = True

    assert f(s) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_20, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "()[]{}"
    output = True

    assert f(s) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_20, predicate=inspect.isfunction)])
def test_example_3(f):
    s = "(]"
    output = False

    assert f(s) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_20, predicate=inspect.isfunction)])
def test_lc_87(f):
    s = "["
    output = False

    assert f(s) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_20, predicate=inspect.isfunction)])
def test_lc_6(f):
    s = "]"
    output = False

    assert f(s) == output
