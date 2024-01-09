import pytest
import inspect
import solution_11


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_11, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
    In this case, the max area of water (blue section) the container can contain is 49.
    """
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = 49

    assert f(height) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_11, predicate=inspect.isfunction)])
def test_example_2(f):
    height = [1, 1]
    output = 1

    assert f(height) == output
