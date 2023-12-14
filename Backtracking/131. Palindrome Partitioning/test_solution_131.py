import pytest
import inspect
import solution_131


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_131, predicate=inspect.isfunction)])
def test_example_1(f):
    s = "aab"
    output = [["a", "a", "b"], ["aa", "b"]]

    assert same_elements(f(s), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_131, predicate=inspect.isfunction)])
def test_example_2(f):
    s = "a"
    output = [["a"]]
    assert same_elements(f(s), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_131, predicate=inspect.isfunction)])
def test_lc_18(f):
    s = "aab"
    output = [["a", "a", "b"], ["aa", "b"]]
    assert same_elements(f(s), output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_131, predicate=inspect.isfunction)])
def test_lc_24(f):
    s = "efe"
    output = [["e", "f", "e"], ["efe"]]
    assert same_elements(f(s), output)
