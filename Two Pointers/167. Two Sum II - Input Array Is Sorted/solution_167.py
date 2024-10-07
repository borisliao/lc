def twoPointers(numbers: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers)-1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left+1, right+1]


def review1(numbers: list[int], target: int) -> list[int]:
    """
    Anki 12-24-23
    Time: 20 min
    O(n) space complexity
    """
    count = {}

    for i, n in enumerate(numbers):
        if target - n in count:
            return [count[target-n]+1, i+1]
        count[n] = i


def review2(numbers: list[int], target: int) -> list[int]:
    """
    Anki 12-24-23
    Time: 10 min
    Used: [Two Sum II - Amazon Coding Interview Question - Leetcode 167 - Python](https://www.youtube.com/watch?v=cQ1Oz4ckceM), debugger 1, solution 1
    """
    l = 0
    r = len(numbers) - 1

    while l < r:  # s1 <=
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1  # d2 l-=1


def review3(numbers: list[int], target: int) -> list[int]:
    """
    Anki 12-29-23
    Time: 9:49
    Used: solution 1, debugger 1
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        total = numbers[l] + numbers[r]
        if target == total:
            # s1 "indices of the two numbers, index1 and index2, added by one as an integer array"
            return [l+1, r+1]
        elif target < total:
            r -= 1
        else:
            l += 1  # d2 l-=1


def review4(numbers: list[int], target: int) -> list[int]:
    """
    Anki 1-2-24
    Time: 7 min
    Used: solution 1
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l+1, r+1]
        elif total > target:  # s1 0 instead of total
            r -= 1
        else:
            l += 1


def review5(numbers: list[int], target: int) -> list[int]:
    """
    Anki 1-16-24
    Time: 8 min
    Used: debugger 1
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l+1, r+1]  # d1 +1, +1
        elif total > target:
            r -= 1
        else:
            l += 1


def review6(numbers: list[int], target: int) -> list[int]:
    """
    Mochi 4-16-24
    Time: 5 min
    """
    l = 0
    r = len(numbers) - 1  # d1 - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]  # d2 +1, +1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1


def review7(numbers: list[int], target: int) -> list[int]:
    """
    Mochi 10-7-24
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1, r+1]
        elif sum < target:
            l += 1
        else:
            r -= 1
