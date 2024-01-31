import inspect
import pytest
import solution_1046


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1046, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
    """
    stones = [2, 7, 4, 1, 8, 1]
    output = 1

    assert f(stones) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1046, predicate=inspect.isfunction)])
def test_example_2(f):
    stones = [1]
    output = 1

    assert f(stones) == output
