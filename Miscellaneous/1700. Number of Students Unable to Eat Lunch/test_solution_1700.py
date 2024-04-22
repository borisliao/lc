import pytest
import inspect
import solution_1700


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1700, predicate=inspect.isfunction)])
def test_example_1(f):
    """
    - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
    - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
    - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
    - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
    - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
    - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
    - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
    - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
    Hence all students are able to eat.
    """
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    output = 0

    assert f(students, sandwiches) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1700, predicate=inspect.isfunction)])
def test_example_2(f):
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    output = 3

    assert f(students, sandwiches) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1700, predicate=inspect.isfunction)])
def test_lc_10(f):
    students = [1, 1]
    sandwiches = [0, 1]
    output = 2

    assert f(students, sandwiches) == output
