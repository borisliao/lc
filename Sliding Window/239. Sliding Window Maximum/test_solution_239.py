from random import randrange
import pytest
import inspect
import solution_239


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_239, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = [3, 3, 5, 5, 6, 7]
    """
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    """

    assert f(nums, k) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_239, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [1]
    k = 1
    output = [1]

    assert f(nums, k) == output


@pytest.mark.timeout(2)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_239, predicate=inspect.isfunction)])
def test_lc_20(f):
    k = 1
    nums = [1, -1]
    output = [1, -1]

    assert f(nums, k) == output


@pytest.mark.timeout(2)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_239, predicate=inspect.isfunction)])
def test_lc_37(f):
    k = 50000
    nums = [randrange(0, 10000) for _ in range((k*2))]
    output = [max(nums)] * (k+1)

    assert f(nums, k) == output


@pytest.mark.timeout(2)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_239, predicate=inspect.isfunction)])
def test_1(f):
    k = 2
    nums = [2, 1, 0]
    output = [2, 1]

    assert f(nums, k) == output
