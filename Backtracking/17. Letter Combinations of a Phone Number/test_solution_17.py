import pytest
import inspect
import solution_17


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_17, predicate=inspect.isfunction)])
def test_example_1(f):
    digits = "23"
    output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    assert same_elements(f(digits), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_17, predicate=inspect.isfunction)])
def test_example_2(f):
    digits = ""
    output = []
    assert f(digits) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_17, predicate=inspect.isfunction)])
def test_lc_24(f):
    digits = "2"
    output = ["a", "b", "c"]
    assert same_elements(f(digits), output)
