import pytest
import inspect
import solution_22


import unittest
case = unittest.TestCase()


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_22, predicate=inspect.isfunction)])
def test_example_1(f):
    n = 3
    output = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    case.assertCountEqual(f(n), output)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_22, predicate=inspect.isfunction)])
def test_example_2(f):
    n = 1
    output = ["()"]

    case.assertCountEqual(f(n), output)
