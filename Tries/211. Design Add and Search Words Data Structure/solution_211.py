def WordDictionary():
    """
    Mochi 4-30-24
    """
    class Trie:
        def __init__(self, c=None):
            self.char = c
            self.next: dict[str: Trie] = {}
            self.word = False

    class WordDictionary:

        def __init__(self):
            self.d = Trie()

        def addWord(self, word: str) -> None:
            node = self.d
            for c in word:
                if c not in node.next:
                    node.next[c] = Trie(c)
                node = node.next[c]
            node.word = True

        def search(self, word: str) -> bool:
            def dfs(i, root):
                node = root

                for index in range(i, len(word)):
                    n = word[index]
                    if n == '.':
                        for child in node.next.values():
                            if dfs(i+1, child):
                                return True
                        return False
                    else:
                        if n not in node.next:
                            return False
                        node = node.next[n]
                return node.word
            return dfs(0, self.d)

    return WordDictionary()

# def WordDictionary():
#     """
#     """
#     class WordDictionary:

#         def __init__(self):
#             pass

#         def addWord(self, word: str) -> None:
#             pass

#         def search(self, word: str) -> bool:
#             pass

#     return WordDictionary()
