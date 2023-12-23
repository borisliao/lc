import inspect
import pytest
import solution_70


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_70, predicate=inspect.isfunction)])
def test_example_1(f):
    n = 2
    output = 2

    assert f(n) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_70, predicate=inspect.isfunction)])
def test_example_2(f):
    n = 3
    output = 3

    assert f(n) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_70, predicate=inspect.isfunction)])
def test_lc_16(f):
    n = 38
    output = 63245986

    assert f(n) == output
