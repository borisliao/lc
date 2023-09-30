import pytest
import inspect
import solution_208


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_208, predicate=inspect.isfunction)])
def test_example_1(f):
    trie = f()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
