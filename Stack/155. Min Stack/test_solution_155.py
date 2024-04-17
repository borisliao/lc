import pytest
import inspect
import solution_155


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_155, predicate=inspect.isfunction)])
def test_example_1(f):
    minStack = f()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_155, predicate=inspect.isfunction)])
def test_lc_7(f):
    minStack = f()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    assert minStack.getMin() == 0
    minStack.pop()
    assert minStack.getMin() == 0


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_155, predicate=inspect.isfunction)])
def test_lc_9(f):
    minStack = f()
    minStack.push(2147483646)
    minStack.push(2147483646)
    minStack.push(2147483647)
    minStack.top()  # assert
    minStack.pop()  # assert
    minStack.getMin()  # assert
    minStack.pop()  # assert
    minStack.getMin()  # assert
    minStack.pop()  # assert
    minStack.push(2147483647)
    minStack.top()  # assert
    minStack.getMin()  # assert
    minStack.push(2147483648)
    minStack.top()  # assert
    minStack.getMin()  # assert
    minStack.pop()  # assert
    minStack.getMin()  # assert
