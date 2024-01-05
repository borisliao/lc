# def attempt1(capacity: int):
#     class Node:
#         def __init__(self, key, value, prev, next):
#             self.key = key
#             self.value = value
#             self.prev = prev
#             self.next = next

#     class LRUCache:
#         def __init__(self, capacity: int):
#             startNode = Node(None, None, None, None)
#             self.data = {'capacity': capacity,
#                          'length': 0,
#                          'start': startNode,
#                          'end': startNode}

#         def get(self, key: int) -> int:
#             if key in self.data:
#                 keyNode = self.data[key]

#                 keyNode.prev.next = keyNode.next

#                 keyNode.prev = self.data['end']
#                 keyNode.next = None

#                 self.data['end'].next = keyNode
#                 self.data['end'] = keyNode

#                 return keyNode.value
#             else:
#                 return -1

#         def put(self, key: int, value: int) -> None:
#             if key in self.data:
#                 self.data[key].prev = self.data[key].next
#                 del self.data[key]
#                 self.data['length'] -= 1

#             putNode = Node(key, value, self.data['end'], None)
#             self.data['end'].next = putNode
#             self.data['end'] = putNode
#             self.data[key] = putNode
#             self.data['length'] += 1

#             if self.data['length'] > self.data['capacity']:
#                 evictedNode = self.data['start'].next

#                 self.data['start'].next = evictedNode.next

#                 del self.data[evictedNode.key]

#                 self.data['length'] -= 1

#     return LRUCache(capacity)


# def review1(capacity: int):
#     """
#     Anki 12-15-23
#     """

#     class Node:
#         def __init__(self, key: int = None, value: int = None, next: "Node" = None, prev: "Node" = None):
#             self.key = key
#             self.value = value
#             self.next = next
#             self.prev = prev

#         def __str__(self):
#             list = []

#             def addToList(ln: Node, list: list):
#                 list.append(ln.value)
#                 if (ln.next):
#                     addToList(ln.next, list)

#             addToList(self, list)

#             return str(list)

#         def __repr__(self):
#             return f"({self.value}, {self.next})"

#     class LRUCache:

#         def __init__(self, capacity: int):
#             """Initialize the LRU cache with positive size capacity."""
#             self.capacity = capacity

#             self.node: dict[int, Node] = {}
#             self.last_node = Node()
#             self.first_node = self.last_node

#         def get(self, key: int) -> int:
#             """
#             Return the value of the key if the key exists, otherwise return -1.
#             Runs in O(1) average time complexity
#             """
#             if key not in self.node:  # d4 if not self.node[key]
#                 return -1

#             node = self.node[key]

#             if len(self.node) == 1:
#                 return node.value

#             node.prev.next = node.next  # s1

#             node.prev = self.first_node  # s1
#             node.next = None

#             self.first_node.next = node  # s1 # error here with the swap
#             self.first_node = node  # s1

#             # self.first_node.next = node
#             # node.prev.next = node.next
#             # node.prev = self.first_node
#             # self.first_node.prev =
#             # node.next = None

#             return node.value

#         def put(self, key: int, value: int) -> None:
#             """
#             Update the value of the key if the key exists.
#             Otherwise, add the key-value pair to the cache.
#             If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#             Runs in O(1) average time complexity
#             """
#             if key in self.node:
#                 self.node[key].value = value
#                 self.get(key)
#                 return

#             new_node = Node(key=key, value=value, prev=self.first_node)
#             self.first_node.next = new_node  # s3
#             self.first_node = new_node
#             self.node[key] = new_node

#             if len(self.node) > self.capacity:
#                 to_be_deleted_node = self.last_node.next
#                 self.last_node.next = to_be_deleted_node.next  # s2
#                 # d5 to_be_deleted_node.value
#                 del self.node[to_be_deleted_node.key]

#     return LRUCache(capacity)

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


# def review2(capacity: int):
#     """
#     Anki 12-17-23
#     """

#     class Node:
#         def __init__(self, prev: "Node" = None, next: "Node" = None, value: int = None) -> None:
#             self.prev = prev
#             self.next = next
#             self.value = value

#     class LRUCache:

#         def __init__(self, capacity: int):
#             """Initialize the LRU cache with positive size capacity."""
#             self.node: dict[int, Node] = {}
#             self.head = Node()
#             self.tail = self.head
#             self.capacity = capacity

#         def get(self, key: int) -> int:
#             """
#             Return the value of the key if the key exists, otherwise return -1.
#             Runs in O(1) average time complexity
#             """
#             if key not in self.node:
#                 return -1

#             WN = self.node[key]

#             # Remove refrences from working node
#             WN.prev.next = WN.next
#             WN.next.prev = WN.prev

#             # Move the working node to the head
#             prev_head = self.head
#             self.head = WN
#             WN.prev = prev_head
#             WN.next = None

#             return WN.value

#         def put(self, key: int, value: int) -> None:
#             """
#             Update the value of the key if the key exists.
#             Otherwise, add the key-value pair to the cache.
#             If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#             Runs in O(1) average time complexity
#             """
#             if key in self.node:
#                 return

#             new_node = Node(prev=self.head, next=None, value=value)
#             self.head.next = new_node
#             self.head = new_node

#             self.node[key] = new_node

#     return LRUCache(capacity)

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

            if len(self.node) > capacity:
                self.remove(self.left.next)
                del self.node[self.left.next.key]

        def remove(self, n: Node):
            prev, nxt = n.prev, n.next  # s1 n.prev = n.next
            prev.next, nxt.prev = nxt, prev  # s1

        def insert(self, n: Node):
            prev, nxt = self.right.prev, self.right  # s1
            prev.next = nxt.prev = n  # s1
            n.next, n.prev = nxt, prev  # s1

    return LRUCache(capacity)


# def review4(capacity: int):
#     """
#     Anki 1-5-24
#     """

#     class Node:
#         def __init__(self, k: int = None, v: int = None):
#             self.key = k
#             self.val = v
#             self.prev = self.next = None

#     class LRUCache:

#         def __init__(self, capacity: int):
#             """Initialize the LRU cache with positive size capacity."""
#             self.capacity = capacity
#             self.node = {}
#             self.left, self.right = Node(), Node()
#             self.left.next, self.right.prev = self.right, self.left

#         def get(self, key: int) -> int:
#             """
#             Return the value of the key if the key exists, otherwise return -1.
#             Runs in O(1) average time complexity
#             """
#             pass

#         def put(self, key: int, value: int) -> None:
#             """
#             Update the value of the key if the key exists.
#             Otherwise, add the key-value pair to the cache.
#             If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#             Runs in O(1) average time complexity
#             """
#             pass

#         def remove(self, n: Node):
#             pass

#         def insert(self, n: Node):
#             pass

#     return LRUCache(capacity)
