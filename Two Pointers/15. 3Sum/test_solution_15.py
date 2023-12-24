import pytest
import inspect
import solution_15


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_15, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    **Explanation:** 
    nums\[0\] + nums\[1\] + nums\[2\] = (-1) + 0 + 1 = 0.
    nums\[1\] + nums\[2\] + nums\[4\] = 0 + 1 + (-1) = 0.
    nums\[0\] + nums\[3\] + nums\[4\] = (-1) + 2 + (-1) = 0.
    The distinct triplets are \[-1,0,1\] and \[-1,-1,2\].
    Notice that the order of the output and the order of the triplets does not matter.
    """
    nums = [-1, 0, 1, 2, -1, -4]
    output = [[-1, -1, 2], [-1, 0, 1]]

    assert same_elements(nums, output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_15, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    **Explanation:** The only possible triplet does not sum up to 0.
    """
    nums = [0, 1, 1]
    output = []

    assert f(nums) == output


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_15, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    **Explanation:** The only possible triplet sums up to 0.
    """
    nums = [0, 0, 0]
    output = [[0, 0, 0]]

    assert f(nums) == output
