# def palidrome2(s: str) -> bool:
#     """
#     Mochi 4-23-24
#     """
#     l = 0
#     r = len(s) - 1

#     char = None  # d1
#     while l < r:
#         if s[l] != s[r]:
#             if not char and l <= r and s[l] == s[r-1]:
#                 char = s[r]  # d1
#                 r -= 1
#             elif not char and l <= r and s[l+1] == s[r]:
#                 char = s[l]  # d1
#                 l += 1
#             else:
#                 return False
#         l += 1
#         r -= 1

#     return True

def neetcode(s: str) -> bool:
    """
    https://www.youtube.com/watch?v=JrxRYBwG6EI
    """
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            sLeft = s[l+1:r+1]
            sRight = s[l:r]

            return (sLeft == sLeft[::-1] or sRight == sRight[::-1])
        l += 1
        r -= 1
    return True
