import pytest
import inspect
import solution_40


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_40, predicate=inspect.isfunction)])
def test_example_1(f):
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    output = [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]

    assert same_elements(f(candidates, target), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_40, predicate=inspect.isfunction)])
def test_example_2(f):
    candidates = [2, 5, 2, 1, 2]
    target = 5
    output = [
        [1, 2, 2],
        [5]
    ]

    assert same_elements(f(candidates, target), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_40, predicate=inspect.isfunction)])
def test_lc_23(f):
    candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    target = 27
    output = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    assert same_elements(f(candidates, target), output)
