def letterCombinations(digits: str) -> list[str]:
    """
    12-12-23
    Time: 23:33
    """
    d_to_a = {  # d1 key needs to be string type
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }
    result = []
    subset = ['']

    def dfs(i):
        if i == len(digits):
            if subset != ['']:
                result.append(subset[0])
            return
        for a in d_to_a[digits[i]]:
            subset[0] += a
            dfs(i+1)
            subset[0] = subset[0][:-1]

    dfs(0)
    return result


def review1(digits: str) -> list[str]:
    """
    Anki 12-18-23
    Time: 9:55
    Used: Solution 3
    """
    d_to_a = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    result = []
    subset = ['']

    def dfs(i):
        if i >= len(digits):
            if subset != ['']:  # s2 edge case for Input: digits = “” Output: []
                result.append(subset[0])  # s3 subset.copy()
            return

        for a in d_to_a[digits[i]]:
            subset[0] += a
            dfs(i+1)
            subset[0] = subset[0][:-1]  # s1 subset[:-1]

    dfs(0)
    return result


# def review2(digits: str) -> list[str]:
#     """
#     Anki
#     """
