import unittest
import pytest
import inspect
import solution_347

import unittest
case = unittest.TestCase()


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_347, predicate=inspect.isfunction)])
def test_example_1(f):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = [1, 2]

    case.assertCountEqual(f(nums, k), output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_347, predicate=inspect.isfunction)])
def test_example_2(f):
    nums = [1]
    k = 1
    output = [1]

    case.assertCountEqual(f(nums, k), output)


@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_347, predicate=inspect.isfunction)])
def test_lc(f):
    nums = [1, 2]
    k = 2
    output = [1, 2]

    case.assertCountEqual(f(nums, k), output)
