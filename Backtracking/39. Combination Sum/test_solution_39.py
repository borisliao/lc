import pytest
import inspect
import solution_39


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_39, predicate=inspect.isfunction)])
def test_example_1(f):
    candidates = [2, 3, 6, 7]
    target = 7
    output = [[2, 2, 3], [7]]

    assert same_elements(f(candidates, target), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_39, predicate=inspect.isfunction)])
def test_example_2(f):
    candidates = [2, 3, 5]
    target = 8
    output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    assert same_elements(f(candidates, target), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_39, predicate=inspect.isfunction)])
def test_example_3(f):
    candidates = [2]
    target = 1
    output = []

    assert same_elements(f(candidates, target), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_39, predicate=inspect.isfunction)])
def test_lc_81(f):
    candidates = [8, 7, 4, 3]
    target = 11
    output = [[8, 3], [7, 4], [4, 4, 3]]

    assert same_elements(f(candidates, target), output)
