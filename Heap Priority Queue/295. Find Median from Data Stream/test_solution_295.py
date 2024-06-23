import pytest
import inspect
import solution_295


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_295, predicate=inspect.isfunction)])
def test_example_1(f):
    medianFinder = f()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    assert medianFinder.findMedian() == 1.5  # return  (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr = [1, 2, 3]
    assert medianFinder.findMedian() == 2.0


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_295, predicate=inspect.isfunction)])
def test_lc_9(f):
    """
    When using 2 heaps, make sure they are actually balanced
    """
    medianFinder = f()
    medianFinder.addNum(1)
    assert medianFinder.findMedian() == 1.00000
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.50000
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.00000
    medianFinder.addNum(4)
    assert medianFinder.findMedian() == 2.50000
    medianFinder.addNum(5)
    assert medianFinder.findMedian() == 3.00000
    medianFinder.addNum(6)
    assert medianFinder.findMedian() == 3.50000
    medianFinder.addNum(7)
    assert medianFinder.findMedian() == 4.00000
    medianFinder.addNum(8)
    assert medianFinder.findMedian() == 4.50000
    medianFinder.addNum(9)
    assert medianFinder.findMedian() == 5.00000
    medianFinder.addNum(10)
    assert medianFinder.findMedian() == 5.50000
