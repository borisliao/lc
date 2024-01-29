import pytest
import inspect
import solution_49

import unittest
case = unittest.TestCase()


def same_elements(x, y):
    sorted_x = sorted([sorted(e) for e in x])
    sorted_y = sorted([sorted(e) for e in y])
    assert sorted_x == sorted_y
    return sorted_x == sorted_y


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_1(f):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert same_elements(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = [""]
    output = [[""]]

    assert same_elements(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_3(f):
    strs = ["a"]
    output = [["a"]]

    assert same_elements(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_lc_24(f):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert same_elements(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_lc_43(f):
    strs = ["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]
    output = [['cry'], ['jon'], ['pus'], [
        'pyx'], ['ram'], ['tin'], ['zip', 'zip']]
    assert same_elements(f(strs), output)
