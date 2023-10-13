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
