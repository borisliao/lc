import pytest
import inspect
import solution_853


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_853, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation:
    The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
    The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
    The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
    Note that no other cars meet these fleets before the destination, so the answer is 3.
    """
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    output = 3

    assert f(target, position, speed) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_853, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: There is only one car, hence there is only one fleet.
    """
    target = 10
    position = [3]
    speed = [3]
    output = 1

    assert f(target, position, speed) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_853, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    Explanation:
    The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
    Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
    """
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    output = 1

    assert f(target, position, speed) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_853, predicate=inspect.isfunction)])
def test_lc_9(f):
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    output = 3

    assert f(target, position, speed) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_853, predicate=inspect.isfunction)])
def test_lc_31(f):
    """
    Tests if the stack is still monotonic increasing when you end the loop:
    Wrong:
    for p, s in reversed(car):
        time = (target-p)/s
        if stack and stack[-1] >= time:
            stack.pop()
        stack.append(time) # wrong

    Right:
    for p, s in reversed(car):
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()
    """
    target = 31
    position = [5, 26, 18, 25, 29, 21, 22, 12, 19, 6]
    speed = [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]
    output = 6

    assert f(target, position, speed) == output
