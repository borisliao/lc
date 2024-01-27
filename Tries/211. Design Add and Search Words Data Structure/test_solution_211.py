import pytest
import inspect
import solution_211


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_211, predicate=inspect.isfunction)])
def test_example_1(f):
    wordDictionary = f()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    assert wordDictionary.search("pad") == False
    assert wordDictionary.search("bad") == True
    assert wordDictionary.search(".ad") == True
    assert wordDictionary.search("b..") == True
