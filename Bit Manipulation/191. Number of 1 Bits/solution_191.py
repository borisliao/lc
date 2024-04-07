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


def review2(n: int) -> int:
    """
    Anki 12-5-23
    Time: 2 min
    """
    count = 0
    while n:
        n = n & (n - 1)
        count += 1

    return count


def review3(n: int) -> int:
    """
    Anki 12-5-23
    Time: 2 min
    """
    count = 0
    while n:
        count += n & 1
        n = n >> 1

    return count


def review4(n: int) -> int:
    """
    Anki 12-10-23
    Used: Solution (1)
    Time: 2 min
    """
    result = 0
    while n:
        result += n & 1
        n >>= 1  # s1 subtracted instead of bitshifted
    return result


def review5(n: int) -> int:
    """
    Anki 12-10-23
    Time: 2 min
    Used: Solution (1)
    """
    result = 0
    while n:
        n = n & (n-1)  # s1 - instead of &
        result += 1
    return result


def review6(n: int) -> int:
    """
    Anki 12-18-23
    Time: 2 min
    """
    count = 0
    while n:
        count += 1
        n = n & (n-1)

    return count


def review7(n: int) -> int:
    """
    12-18-23
    Time: 1 min
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1

    return count


def review8(n: int) -> int:
    """
    Anki 1-10-24
    Time: 3 min
    Used: Debugger 1
    """
    one_bits = 0
    while n:
        one_bits += n & 1
        n >>= 1  # d1 n >>= n
    return one_bits


def review8(n: int) -> int:
    """
    Mochi 4-7-24
    Time: 4 min
    """
    amount = 0

    while n:
        amount += n & 1
        n >>= 1

    return amount


def review9(n: int) -> int:
    """
    Mochi 4-7-24
    Time: 4 min
    """
    amount = 0

    while n:
        n = n & (n - 1)
        amount += 1

    return amount
