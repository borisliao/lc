import pytest
import inspect
import solution_49

import unittest
case = unittest.TestCase()


# def SameStuff(l1, l2):
#     if not l1 and not l2:
#         return True

#     if len(l1) != len(l2):
#         return False

#     last_element = l1[-1]
#     if last_element not in l2:
#         return False

#     l1.remove(last_element)
#     l2.remove(last_element)

#     return SameStuff(l1, l2)


# # does not work due to nested list not being in the right order
# @pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
# def test_example_1(f):
#     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

#     assert SameStuff(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_2(f):
    strs = [""]
    output = [[""]]

    case.assertCountEqual(f(strs), output)


@ pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_49, predicate=inspect.isfunction)])
def test_example_3(f):
    strs = ["a"]
    output = [["a"]]

    case.assertCountEqual(f(strs), output)
