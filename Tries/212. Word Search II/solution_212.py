# def findWords(board: list[list[str]], words: list[str]) -> list[str]:
#     class Trie:
#         def __init__(self, word=False):
#             self.word = word
#             self.next = {}

#     trie = Trie()

#     result = []
#     subset = []

#     def dfs(r: int, c: int, node: Trie, visited: set):
#         if (r, c) in visited or r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
#             return
#         for char in node.next:
#             if board[r][c] != char:
#                 return
#             visited.add((r, c))
#             dfs(r+1, c, node.next[board[r][c]], visited)
#             dfs(r-1, c, node.next[board[r][c]], visited)
#             dfs(r, c+1, node.next[board[r][c]], visited)
#             dfs(r, c-1, node.next[board[r][c]], visited)
#             visited.remove((r, c))
#         if node.word:
#             result.append(''.join(subset))

#     for w in words:
#         node = trie
#         for c in w:
#             if c not in node.next:
#                 node.next[c] = Trie()
#         node.word = True

#     for r in range(len(board)):
#         for c in range(len(board[r])):
#             node = trie
#             char = board[r][c]
#             if char in node.next:
#                 dfs(r, c, node, set())

#     return result
