import inspect
import pytest
import solution_621


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_621, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    Explanation: 
    A -> B -> idle -> A -> B -> idle -> A -> B
    There is at least 2 units of time between any two same tasks.
    """
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    output = 8

    assert f(tasks, n) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_621, predicate=inspect.isfunction)])
def test_example_2(f):
    """
    Explanation: On this case any permutation of size 6 would work since n = 0.
    ["A","A","A","B","B","B"]
    ["A","B","A","B","A","B"]
    ["B","B","B","A","A","A"]
    ...
    And so on.
    """
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    output = 6

    assert f(tasks, n) == output


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_621, predicate=inspect.isfunction)])
def test_example_3(f):
    """
    Explanation: 
    One possible solution is
    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
    """
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    output = 16

    assert f(tasks, n) == output
