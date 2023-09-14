def attempt1(capacity: int):
    class Node:
        def __init__(self, key, value, prev, next):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    class LRUCache:
        def __init__(self, capacity: int):
            startNode = Node(None, None, None, None)
            self.data = {'capacity': capacity,
                         'length': 0,
                         'start': startNode,
                         'end': startNode}

        def get(self, key: int) -> int:
            if key in self.data:
                keyNode = self.data[key]

                keyNode.prev.next = keyNode.next

                keyNode.prev = self.data['end']
                keyNode.next = None

                self.data['end'].next = keyNode
                self.data['end'] = keyNode

                return keyNode.value
            else:
                return -1

        def put(self, key: int, value: int) -> None:
            if key in self.data:
                self.data[key].prev = self.data[key].next
                del self.data[key]
                self.data['length'] -= 1

            putNode = Node(key, value, self.data['end'], None)
            self.data['end'].next = putNode
            self.data[key] = putNode
            self.data['length'] += 1

            if self.data['length'] > self.data['capacity']:
                evictedNode = self.data['start'].next

                evictedNode.prev.next = evictedNode.next

                del self.data[evictedNode.value]

                self.data['length'] -= 1

    return LRUCache(capacity)
