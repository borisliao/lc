import pytest
import inspect
import solution_973


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_973, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    ![https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
    """
    points = [[1, 3], [-2, 2]]
    k = 1
    output = [[-2, 2]]

    assert f(points, k) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_973, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.
    """
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    output = [[3, 3], [-2, 4]]

    assert same_elements(f(points, k), output)
