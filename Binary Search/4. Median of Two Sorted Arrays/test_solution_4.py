import pytest
import inspect
import solution_4


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_4, predicate=inspect.isfunction)])
def test_example_1(f):
    nums1 = [1, 3]
    nums2 = [2]
    output = 2.00000
    """
    Explanation: merged array = [1,2,3] and median is 2.
    """

    assert f(nums1, nums2) == output


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_4, predicate=inspect.isfunction)])
def test_example_2(f):
    nums1 = [1, 2]
    nums2 = [3, 4]
    output = 2.50000
    """
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    """

    assert f(nums1, nums2) == output
