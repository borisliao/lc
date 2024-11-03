
def neetcode(capacity: int):
    """https://www.youtube.com/watch?v=7ABFKPK2hD4"""
    class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev: Node = None
            self.next: Node = None

    class LRUCache:
        def __init__(self, capacity: int):
            self.cap = capacity
            self.cache = {}  # map key to node

            self.left, self.right = Node(0, 0), Node(0, 0)
            self.left.next, self.right.prev = self.right, self.left

        # remove node from list
        def remove(self, node: Node):
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

        # insert node at right
        def insert(self, node: Node):
            prev, nxt = self.right.prev, self.right
            prev.next = nxt.prev = node
            node.next, node.prev = nxt, prev

        def get(self, key: int) -> int:
            if key in self.cache:
                self.remove(self.cache[key])
                self.insert(self.cache[key])
                return self.cache[key].val
            return -1

        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.cap:
                # remove from the list and delete the LRU from hashmap
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

    return LRUCache(capacity)


def review3(capacity: int):
    """
    NOTE: Study https://www.youtube.com/watch?v=7ABFKPK2hD4 before attempting
    Anki 1-5-24
    """

    class Node:
        def __init__(self, k: int = None, v: int = None, p: "Node" = None, n: "Node" = None):
            self.key = k
            self.val = v
            self.prev = p
            self.next = n

    class LRUCache:

        def __init__(self, capacity: int):
            """Initialize the LRU cache with positive size capacity."""
            self.capacity = capacity
            self.node = {}
            self.left, self.right = Node(), Node()
            self.left.next, self.right.prev = self.right, self.left

        def get(self, key: int) -> int:
            """
            Return the value of the key if the key exists, otherwise return -1.
            Runs in O(1) average time complexity
            """
            if key in self.node:
                self.remove(self.node[key])
                self.insert(self.node[key])
                return self.node[key].val  # s1 .val
            return -1

        def put(self, key: int, value: int) -> None:
            """
            Update the value of the key if the key exists.
            Otherwise, add the key-value pair to the cache.
            If the number of keys exceeds the capacity from this operation, evict the least recently used key.
            Runs in O(1) average time complexity
            """
            if key in self.node:
                self.remove(self.node[key])

            self.node[key] = Node(key, value)  # s1
            self.insert(self.node[key])

            if len(self.node) > self.capacity:  # gpt2 capacity
                lru = self.left.next  # s3
                self.remove(lru)
                del self.node[lru.key]

        def remove(self, n: Node):
            prev, nxt = n.prev, n.next  # s1 n.prev = n.next
            prev.next, nxt.prev = nxt, prev  # s1

        def insert(self, n: Node):
            prev, nxt = self.right.prev, self.right  # s1
            prev.next = nxt.prev = n  # s1
            n.next, n.prev = nxt, prev  # s1

    return LRUCache(capacity)


def review4(capacity: int):
    """
    Anki 1-6-24
    Time: 1h 8m
    """

    class Node:
        def __init__(self, k: int = None, v: int = None):
            self.key = k
            self.val = v
            self.prev = self.next = None

    class LRUCache:

        def __init__(self, capacity: int):
            """Initialize the LRU cache with positive size capacity."""
            self.capacity = capacity
            self.cache = {}
            self.left, self.right = Node(), Node()
            self.left.next, self.right.prev = self.right, self.left

        def get(self, key: int) -> int:
            """
            Return the value of the key if the key exists, otherwise return -1.
            Runs in O(1) average time complexity
            """
            if key in self.cache:
                self.remove(self.cache[key])
                self.insert(self.cache[key])
                return self.cache[key].val
            return -1

        def put(self, key: int, value: int) -> None:
            """
            Update the value of the key if the key exists.
            Otherwise, add the key-value pair to the cache.
            If the number of keys exceeds the capacity from this operation, evict the least recently used key.
            Runs in O(1) average time complexity
            """
            new_node = Node(key, value)
            if key in self.cache:
                self.remove(self.cache[key])
            self.insert(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:  # gpt1 capacity
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]  # gpt2 lru.val

        def remove(self, n: Node):
            n.prev.next = n.next
            n.next.prev = n.prev

        def insert(self, n: Node):
            n.next = self.right
            n.prev = self.right.prev
            self.right.prev.next = n
            self.right.prev = n

    return LRUCache(capacity)


def review5(capacity: int):
    """
    Anki 1-6-24
    Time: 25 min
    Used: gpt 1, debugger 1
    """
    class Node:
        def __init__(self, k=None, v=None):
            self.key = k
            self.value = v
            self.prev: Node = None
            self.next: Node = None

    class LRUCache:
        def __init__(self, capacity: int):
            """Initialize the LRU cache with positive size capacity."""
            self.cache: dict[int, Node] = {}
            self.capacity = capacity
            self.left, self.right = Node(), Node()
            self.left.next, self.right.prev = self.right, self.left

        def get(self, key: int) -> int:
            """
            Return the value of the key if the key exists, otherwise return -1.
            Runs in O(1) average time complexity
            """
            if key in self.cache:
                self.remove(self.cache[key])
                self.insert(self.cache[key])
                return self.cache[key].value
            return -1

        def put(self, key: int, value: int) -> None:
            """
            Update the value of the key if the key exists.
            Otherwise, add the key-value pair to the cache.
            If the number of keys exceeds the capacity from this operation, evict the least recently used key.
            Runs in O(1) average time complexity
            """
            if key in self.cache:
                self.remove(self.cache[key])

            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.capacity:
                del self.cache[self.left.next.key]  # gpt2 .value
                self.remove(self.left.next)

        def remove(self, node: Node):
            p, n = node.prev, node.next
            p.next, n.prev = n, p

        def insert(self, node: Node):
            L, R = self.right.prev, self.right  # d1 .left .right
            node.prev, node.next = L, R  # d1 .left .right
            L.next, R.prev = node, node

    return LRUCache(capacity)


def review6(capacity: int):
    """
    Anki 1-16-24
    Time: 25 min
    """

    class Node:
        def __init__(self, k=None, v=None):
            self.key = k
            self.val = v
            self.next: Node = None
            self.prev: Node = None

    class LRUCache:
        def __init__(self, capacity: int):
            self.size = capacity
            self.head = Node()
            self.tail = Node()
            self.list: dict[int, Node] = {}
            self.head.prev, self.tail.next = self.tail, self.head

        def get(self, key: int) -> int:
            if key in self.list:
                node = self.list[key]
                self.remove(node)
                self.insert(node)
                return node.val
            return -1

        def put(self, key: int, value: int) -> None:
            new_node = Node(key, value)
            if key in self.list:
                self.remove(self.list[key])
                self.list[key] = new_node
            self.insert(new_node)
            self.list[key] = new_node

            if len(self.list) > self.size:
                LRU = self.tail.next
                self.remove(LRU)
                del self.list[LRU.key]

        def remove(self, node: Node):
            left, right = node.prev, node.next
            left.next, right.prev = right, left

        def insert(self, node: Node):
            left, right = self.head.prev, self.head
            left.next, right.prev = node, node
            node.prev, node.next = left, right

    return LRUCache(capacity)


def review7(capacity: int):
    """
    Anki 2-6-24
    Time: 29 min
    Used: solution 1, debugger 2
    """
    class Node:
        def __init__(self, k, v, p, n):
            self.key = k
            self.val = v
            self.prev = p
            self.next = n

    class LRUCache:
        def __init__(self, capacity: int):
            self.head = Node(0, 0, None, None)
            self.tail = Node(0, 0, None, None)
            self.head.next, self.tail.prev = self.tail, self.head
            self.capacity = capacity
            self.lookup = {}

        def get(self, key: int) -> int:
            if key in self.lookup:
                node = self.lookup[key]
                del self.lookup[key]
                self.remove(node)
                self.put(node.key, node.val)
                return node.val
            return -1

        def put(self, key: int, value: int) -> None:
            if key in self.lookup:
                self.remove(self.lookup[key])
                del self.lookup[key]
            node = Node(key, value, None, None)
            l = self.tail.prev
            l.next = node
            self.tail.prev = node
            node.prev = l
            node.next = self.tail

            self.lookup[key] = node

            if len(self.lookup) > self.capacity:  # d2 ==
                evicted = self.head.next
                self.remove(evicted)
                del self.lookup[evicted.key]  # s3 .key

        def remove(self, n):
            l = n.prev  # d1 n.left
            r = n.next  # d1 n.right

            l.next, r.prev = r, l

    return LRUCache(capacity)


def review8(capacity: int):
    """
    Mochi 10-31-24
    """
    class Node:
        def __init__(self, k=None, v=None):
            self.key = k
            self.val = v
            self.next: Node = None
            self.prev: Node = None

    class LRUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.head = Node()
            self.tail = Node()
            self.head.prev = self.tail
            self.tail.next = self.head
            self.store = {}

        def get(self, key: int) -> int:
            if key not in self.store:
                return -1
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val

        def put(self, key: int, value: int) -> None:
            new_node = Node(key, value)
            if key in self.store:
                self.remove(self.store[key])
                self.store[key] = new_node
            self.insert(new_node)
            self.store[key] = new_node

            if len(self.store) > self.capacity:
                LRU = self.tail.next
                self.remove(LRU)
                del self.store[LRU.key]

        def remove(self, node: Node) -> None:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

        def insert(self, node: Node) -> None:  # s1
            left, right = self.head.prev, self.head
            left.next, right.prev = node, node
            node.prev, node.next = left, right

    return LRUCache(capacity)

# def review(capacity: int):
#     """
#     Mochi
#     """

#     class LRUCache:
#         def __init__(self, capacity: int):
#             pass

#         def get(self, key: int) -> int:
#             pass

#         def put(self, key: int, value: int) -> None:
#             pass

#     return LRUCache(capacity)
