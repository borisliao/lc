import pytest
import inspect
import solution_739


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_739, predicate=inspect.isfunction)])
def test_example_1(f):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [1, 1, 4, 2, 1, 1, 0, 0]

    assert f(temperatures) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_739, predicate=inspect.isfunction)])
def test_example_2(f):
    temperatures = [30, 40, 50, 60]
    output = [1, 1, 1, 0]

    assert f(temperatures) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_739, predicate=inspect.isfunction)])
def test_example_3(f):
    temperatures = [30, 60, 90]
    output = [1, 1, 0]

    assert f(temperatures) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_739, predicate=inspect.isfunction)])
def test_lc_5(f):
    temperatures = [34, 80, 80, 34, 34, 80, 80, 80, 80, 34]
    output = [1, 0, 0, 2, 1, 0, 0, 0, 0, 0]

    assert f(temperatures) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_739, predicate=inspect.isfunction)])
def test_lc_6(f):
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    output = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]

    assert f(temperatures) == output
