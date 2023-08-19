import pytest
import inspect
import solution_191


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_191, predicate=inspect.isfunction)])
def test_example_1(f):
    n = 11
    output = 3

    assert f(n) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_191, predicate=inspect.isfunction)])
def test_example_2(f):
    n = 128
    output = 1

    assert f(n) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_191, predicate=inspect.isfunction)])
def test_example_3(f):
    n = 4294967293
    output = 31

    assert f(n) == output
