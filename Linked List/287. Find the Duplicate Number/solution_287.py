def neetcode(nums: list[int]) -> int:
    """
    https://www.youtube.com/watch?v=wjYnzkAhcNk
    Use flynns tortise and hare algo
    recognizing it is a linked list nums array
    """
    fast, slow = 0, 0

    # find intersection of fast and slow
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]

        if fast == slow:
            break

    # find start of cyclical graph (will be the number of the duplicate)
    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]

        if slow == slow2:
            return slow


def review1(nums: list[int]) -> int:
    """
    Mochi 4-22-24
    """
    fast, slow = 0, 0

    # find intersection of fast and slow
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]

        if fast == slow:
            break

    # find start of cyclical graph (will be the number of the duplicate)
    result = nums[0]
    slow = nums[slow]
    while result != slow:
        result = nums[result]
        slow = nums[slow]

    return result


def review2(nums: list[int]) -> int:
    """
    Mochi 4-24-24
    """
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    head = 0
    while True:
        slow = nums[slow]
        head = nums[head]

        if slow == head:
            return slow


def review3(nums: list[int]) -> int:
    """
    Mochi 4-25-24
    """
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    node = 0
    while True:
        slow = nums[slow]
        node = nums[node]

        if slow == node:
            return node


def review4(nums: list[int]) -> int:
    slow, fast = 0, 0

    # floyd is can find the beginning of a cycle

    # find the distance between the end of the cycle
    while True:
        slow = nums[slow]  # move 1 in the cycle
        fast = nums[nums[fast]]  # move 2 in the cycle

        if slow == fast:
            break

    # race the slow and fast pointer by 1 to find the start of the cycle
    node = 0
    while True:
        slow = nums[slow]
        node = nums[node]

        if slow == node:
            return node
