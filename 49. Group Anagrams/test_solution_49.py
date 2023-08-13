import pytest
import inspect
import solution_49

import unittest
case = unittest.TestCase()

# does not work due to nested list not being in the right order
# @pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
# def test_example_1(f):
#     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

#     case.assertCountEqual(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = [""]
    output = [[""]]

    case.assertCountEqual(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = ["a"]
    output = [["a"]]

    case.assertCountEqual(f(strs), output)
