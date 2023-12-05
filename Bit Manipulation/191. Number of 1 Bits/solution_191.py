def naive(n: int) -> int:
    count = 0
    for i in format(n, 'b'):
        if i == '1':
            count += 1

    return count


def review1(n: int) -> int:
    """
    Anki 12-5-23
    Used: [Number of 1 Bits - Leetcode 191 - Python](https://www.youtube.com/watch?v=5Km3utixwZs)
    """
    count = 0
    while n:
        count += n & 1
        n = n >> 1

    return count


def neetcode_1(n: int) -> int:
    """
    12-5-23
    [Number of 1 Bits - Leetcode 191 - Python](https://www.youtube.com/watch?v=5Km3utixwZs)
    """
    count = 0
    while n:
        count += n % 2
        n = n >> 1

    return count


def neetcode_2(n: int) -> int:
    """
    12-5-23
    [Number of 1 Bits - Leetcode 191 - Python](https://www.youtube.com/watch?v=5Km3utixwZs)
    """
    res = 0
    while n:
        n &= n - 1  # n & (n-1)
        res += 1
    return res
