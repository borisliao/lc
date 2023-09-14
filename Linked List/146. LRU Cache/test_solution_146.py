import pytest
import inspect
import solution_146


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_146, predicate=inspect.isfunction)])
def test_example_1(f):
    lRUCache = f(2)

    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lRUCache.get(1) == -1  # return -1 (not found)
    assert lRUCache.get(3) == 3  # return 3
    assert lRUCache.get(4) == 4  # return 4
