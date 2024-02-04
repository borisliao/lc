
import inspect
import pytest
import solution_417


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_417, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)
    Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    [0,4]: [0,4] -> Pacific Ocean 
        [0,4] -> Atlantic Ocean
    [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
        [1,3] -> [1,4] -> Atlantic Ocean
    [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
        [1,4] -> Atlantic Ocean
    [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    [3,0]: [3,0] -> Pacific Ocean 
        [3,0] -> [4,0] -> Atlantic Ocean
    [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
        [3,1] -> [4,1] -> Atlantic Ocean
    [4,0]: [4,0] -> Pacific Ocean 
        [4,0] -> Atlantic Ocean
    Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
    """
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
        2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    assert f(heights) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_417, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
    """
    heights = [[1]]
    output = [[0, 0]]

    assert f(heights) == output
