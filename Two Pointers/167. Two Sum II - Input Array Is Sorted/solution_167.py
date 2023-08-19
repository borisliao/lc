from typing import List


# def nsquared(numbers: List[int], target: int) -> List[int]:
#     """
#     Time Complexity: O(n^2)
#     Space Complexity: O(1)
#     """
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if i != j:
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]


def twoPointers(numbers: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers)-1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -=1
        elif numbers[left] + numbers[right] < target:
            left +=1
        else:
            return [left+1,right+1]