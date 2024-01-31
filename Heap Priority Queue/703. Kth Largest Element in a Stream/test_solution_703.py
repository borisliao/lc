import pytest
import inspect
import solution_703


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_703, predicate=inspect.isfunction)])
def test_example_1(f):
    kthLargest = f()(3, [4, 5, 8, 2])
    assert 4 == kthLargest.add([3])
    assert 5 == kthLargest.add([5])
    assert 5 == kthLargest.add([10])
    assert 8 == kthLargest.add([9])
    assert 8 == kthLargest.add([4])
