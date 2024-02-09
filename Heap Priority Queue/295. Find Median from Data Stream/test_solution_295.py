import pytest
import inspect
import solution_295


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_295, predicate=inspect.isfunction)])
def test_example_1(f):
    medianFinder = f()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    assert f.findMedian() == 1.5  # return  (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr = [1, 2, 3]
    assert f.findMedian() == 2.0
