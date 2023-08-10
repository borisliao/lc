import pytest
import inspect
import solution_1

import unittest
case = unittest.TestCase()

@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [2,7,11,15]
    target = 9
    output = [0,1]
    
    case.assertCountEqual(f(nums, target), output)

@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [3,2,4]
    target = 6
    output = [1,2]
    
    case.assertCountEqual(f(nums, target), output)

@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_1, predicate=inspect.isfunction)])
def test_example_3(f):
    nums = [3,3]
    target = 6
    output = [0,1]
    
    case.assertCountEqual(f(nums, target), output)

