from typing import Dict


# def attempt1():
#     class LinkedList:
#         def __init__(self, val: str, next: {}) -> None:
#             self.val = val
#             self.next = next

#     class Trie:

#         def __init__(self):
#             nodes: Dict[str, LinkedList] = {}

#         def insert(self, word: str) -> None:
#             lastChar = None
#             lastNode = None

#             for char in word:
#                 if char not in self.nodes:
#                     self.nodes[char] = LinkedList(char)
#                     lastChar = None
#                 else:
#                     lastNode = self.nodes[char]
#                     lastNode.

#         def search(self, word: str) -> bool:
#             pass

#         def startsWith(self, prefix: str) -> bool:
#             pass

#     return Trie()

def neetcode():
    """
    https://www.youtube.com/watch?v=oobqoCJlHA0
    All 3 functions use the same way of traversing through the list
    """
    class TreeNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    class Trie:

        def __init__(self):
            self.nodes = TreeNode()

        def insert(self, word: str) -> None:
            current = self.nodes

            for c in word:
                if c not in current.children:
                    current.children[c] = TreeNode()
                current = current.children[c]

            current.isWord = True

        def search(self, word: str) -> bool:
            current = self.nodes

            for c in word:
                if c not in current.children:
                    return False
                current = current.children[c]

            if current.isWord:
                return True

            return False

        def startsWith(self, prefix: str) -> bool:
            current = self.nodes

            for c in prefix:
                if c not in current.children:
                    return False
                current = current.children[c]

            return True

    return Trie()


def review1():
    """
    Anki 1-24-24
    Time: 22 min
    """
    class Node:
        def __init__(self, c: str = None, word=False):  # d1 c: str
            self.c = c
            self.next: dict[str, Node] = {}
            self.word = word

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, word: str) -> None:
            node = self.head
            for c in word:
                if c not in node.next:  # d1 c in node.next
                    node.next[c] = Node(c)
                node = node.next[c]  # d1 else:

            node.word = True

        def search(self, word: str) -> bool:
            node = self.head
            for c in word:
                if c not in node.next:
                    return False
                node = node.next[c]
            return node.word

        def startsWith(self, prefix: str) -> bool:
            node = self.head
            for c in prefix:
                if c not in node.next:
                    return False
                node = node.next[c]  # d2
            return True

    return Trie()


def review2():
    """
    Anki 1-24-24
    Time: 5:25
    """
    class Node:
        def __init__(self, c: str = None, word=False):
            self.c = c
            self.word = word
            self.next: dict[str, "Node"] = {}

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, word: str) -> None:
            node = self.head
            for c in word:
                if c not in node.next:
                    node.next[c] = Node(c)
                node = node.next[c]
            node.word = True

        def search(self, word: str) -> bool:
            node = self.head
            for c in word:
                if c not in node.next:
                    return False
                node = node.next[c]
            return node.word

        def startsWith(self, prefix: str) -> bool:
            node = self.head
            for c in prefix:
                if c not in node.next:
                    return False
                node = node.next[c]
            return True

    return Trie()


def review3():
    """
    Anki 1-29-24
    Time: 8 min
    Used: debugger 1
    """
    class Node:
        def __init__(self, char: str = None, next: dict[str, "Node"] = {}, word=False):
            self.c = char
            self.next = next
            self.word = word

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, word: str) -> None:
            node = self.head
            for c in word:
                if c not in node.next:  # d1 if c not in node
                    node.next[c] = Node(c)
                node = node.next[c]
            node.word = True

        def search(self, word: str) -> bool:
            node = self.head
            for c in word:
                if c not in node.next:
                    return False
                node = node.next[c]
            return node.word

        def startsWith(self, prefix: str) -> bool:
            node = self.head
            for c in prefix:
                if c not in node.next:
                    return False
                node = node.next[c]
            return True

    return Trie()


def review4():
    """
    Mochi 4-13-24
    """
    class Node:
        def __init__(self):
            self.word = False
            self.next: dict[str, Node] = {}

    class Trie:
        def __init__(self):
            self.db = Node()

        def insert(self, word: str) -> None:
            trie = self.db
            for c in word:
                if c not in trie.next:
                    new_node = Node()
                    trie.next[c] = new_node
                    trie = new_node
                else:
                    trie = trie.next[c]
            trie.word = True

        def search(self, word: str) -> bool:
            trie = self.db
            for c in word:
                if c not in trie.next:
                    return False
                trie = trie.next[c]

            return trie.word

        def startsWith(self, prefix: str) -> bool:
            trie = self.db
            for c in prefix:
                if c not in trie.next:
                    return False
                trie = trie.next[c]
            return True

    return Trie()

# def review5():
#     """
#     Mochi 4-13-24
#     """
#     class Trie:
#         def __init__(self):
#             pass

#         def insert(self, word: str) -> None:
#             pass

#         def search(self, word: str) -> bool:
#             pass

#         def startsWith(self, prefix: str) -> bool:
#             pass

#     return Trie()
