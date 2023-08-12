from typing import List


def invalid_solution(nums: List[int]) -> int:
    """This does not satisfy time and memory complexity."""
    values = []
    for i in nums:
        if i not in values:
            values.append(i)
        else:
            values.remove(i)
    return values[0]
