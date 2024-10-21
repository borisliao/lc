import pytest
import inspect
import solution_42


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_42, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.
    """
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    output = 6

    assert f(height) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_42, predicate=inspect.isfunction)])
def test_example_2(f):
    height = [4, 2, 0, 3, 2, 5]
    output = 9

    assert f(height) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_42, predicate=inspect.isfunction)])
def test_lc_82(f):
    """
    Check if you are updating maxR
    """
    height = [4, 2, 3]
    output = 1

    assert f(height) == output
