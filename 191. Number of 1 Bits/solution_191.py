def naive(n: int) -> int:
    count = 0
    for i in format(n, 'b'):
        if i == '1':
            count += 1

    return count
