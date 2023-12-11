import pytest
import inspect
import solution_138
Node = solution_138.Node


def ln(list):
    """From a list, builds a Node data structure with random variable"""
    node_list = []
    dummy = Node(-1)
    node = dummy

    for l in list:
        new_node = Node(l[0])
        node.next = new_node
        node = node.next

        node_list.append(new_node)

    node = dummy.next
    for l in list:
        node.random = node_list[l[1]] if l[1] != None else None
        node = node.next

    return dummy.next


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_1(f):
    head = ln([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    output = ln([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_2(f):
    head = ln([[1, 1], [2, 1]])
    output = ln([[1, 1], [2, 1]])

    assert str(f(head)) == str(output)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_138, predicate=inspect.isfunction)])
def test_example_3(f):
    head = ln([[3, None], [3, 0], [3, None]])
    output = ln([[3, None], [3, 0], [3, None]])

    assert str(f(head)) == str(output)
