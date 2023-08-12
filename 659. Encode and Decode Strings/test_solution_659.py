import pytest
import inspect
import solution_659

@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_659, predicate=inspect.isfunction)])
def test_example_1(f):
    input = ["lint","code","love","you"]
    output = ["lint","code","love","you"]

    assert f('decode')(f('encode')(input)) == output

@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_659, predicate=inspect.isfunction)])
def test_example_2(f):
    input = ["we", "say", ":", "yes"]
    output = ["we", "say", ":", "yes"]
    
    assert f('decode')(f('encode')(input)) == output