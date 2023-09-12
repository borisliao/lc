import pytest
import inspect
import solution_138


def ln(list):
    # TODO: make this work
    """From a list, builds a Node data structure"""
    # if (list):
    #     for n in list:
    #         return solution_138.Node(list[0], ln(list[1:]))
    # else:
    #     return None
    return list


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_1(f):
    head = ln([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    output = ln([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    # assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_2(f):
    head = ln([[1, 1], [2, 1]])
    output = ln([[1, 1], [2, 1]])

    # assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_3(f):
    head = ln([[3, None], [3, 0], [3, None]])
    output = ln([[3, None], [3, 0], [3, None]])

    # assert str(f(head)) == str(output)
