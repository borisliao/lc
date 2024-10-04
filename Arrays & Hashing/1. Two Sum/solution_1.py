from collections import defaultdict


def naive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]


def complement(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        idealNumber = target - nums[i]
        for j in range(len(nums)):
            if i != j:
                if nums[j] == idealNumber:
                    return [i, j]


def doubleItterate(nums: list[int], target: int) -> list[int]:
    indexArray = {}

    for i in range(len(nums)):
        indexArray[nums[i]] = i

    for i in range(len(nums)):
        ideal_number = target - nums[i]
        if ideal_number in indexArray:
            if i != indexArray[ideal_number]:
                return [i, indexArray[ideal_number]]


def twoSum(nums: list[int], target: int) -> list[int]:
    """Hashmap and complement"""
    indexArray = {}

    for i in range(len(nums)):
        ideal_number = target - nums[i]
        if ideal_number in indexArray:
            if i != indexArray[ideal_number]:
                return [i, indexArray[ideal_number]]
        indexArray[nums[i]] = i


def review1(nums: list[int], target: int) -> list[int]:
    """Anki Review 10/11/23"""
    history = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in history:
            return [i, history[complement]]
        else:
            history[n] = i


def review2(nums: list[int], target: int) -> list[int]:
    """Anki Review 10/27/23"""

    # key: number in nums
    # value: index
    previous_nums: dict[int, int] = {}

    for i, n in enumerate(nums):
        complement = target - n

        if complement in previous_nums:
            return [previous_nums[complement], i]

        previous_nums[n] = i


def review3(nums: list[int], target: int) -> list[int]:
    """
    Anki 12-3-23
    Time: 21:27
    """
    nums_dict = defaultdict(lambda: [])

    for i, n in enumerate(nums):
        nums_dict[n].append(i)

    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums_dict:
            for c_index in nums_dict[complement]:
                if c_index != i:
                    return [i, c_index]


def review4(nums: list[int], target: int) -> list[int]:
    """
    Mochi 10-4-24
    """
    dictNums = {n: i for i, n in enumerate(nums)}

    for i, n in enumerate(nums):
        comp = target - n
        if comp in dictNums:
            if i != dictNums[comp]:
                return [i, dictNums[comp]]


def review5(nums: list[int], target: int) -> list[int]:
    """
    Mochi 10-4-24
    continue from review4
    """
    dictNums = {}

    for i, n in enumerate(nums):
        comp = target - n
        if comp in dictNums:
            return [i, dictNums[comp]]

        dictNums[n] = i
