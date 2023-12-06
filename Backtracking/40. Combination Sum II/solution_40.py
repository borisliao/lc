# def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
#     """
#     12-5-23
#     """
#     result = set()
#     combination = []

#     def dfs(i):
#         if sum(combination) == target:
#             result.add(tuple(sorted(combination)))  # d2
#             return
#         if i > len(candidates) - 1 or sum(combination) > target:
#             return

#         combination.append(candidates[i])
#         dfs(i+1)
#         combination.pop()
#         dfs(i+1)

#     dfs(0)  # d1
#     return [list(x) for x in result]
