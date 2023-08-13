import pytest
import inspect
import solution_49

import unittest
case = unittest.TestCase()


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_1(f):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert f(strs) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = [""]
    output = [[""]]

    assert f(strs) == output


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = ["a"]
    output = [["a"]]

    assert f(strs) == output
