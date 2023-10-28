from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Using Dynamic Programming (DP)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    output = []

    pre = 1
    for i in range(len(nums)):
        output.append(pre)
        if pre != len(nums):
            pre *= nums[i]

    post = 1
    for i in reversed(range(len(nums))):
        output[i] *= post
        if post != 0:
            post *= nums[i]

    return output

# def naive(nums: List[int]) -> List[int]:
#     """
#     Time Complexity: O(n^2)
#     Space Complexity: O(n)
#     """
#     arr = []
#     for i in range(len(nums)):
#         if i+1 > len(nums):
#             maxrange = i
#         else:
#             maxrange = i+1
#         x = nums[:i] + nums[maxrange:]


#         product = 1
#         for y in x:
#             product *= y

#         arr.append(product)

#     return arr

def review1(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    Anki review 10/22/23
    """
    left = {}
    product = 1
    for i, n in enumerate(nums):
        product *= n
        left[i] = product

    right = {}
    product = 1
    i = 0
    for n in nums[::-1]:
        product *= n
        right[i] = product
        i += 1

    l = 0
    r = len(nums) - 2
    result = []
    while len(result) < len(nums):
        product = 1
        if r > -1:
            product *= right[r]
            r -= 1
        if len(result) > 0:
            product *= left[l]
            l += 1
        result.append(product)

    return result

def review2(nums: List[int]) -> List[int]:
    """Anki Reviewed 10/28/23"""
    result = []

    pre = 1
    for i in range(len(nums)):
        result.append(pre)
        pre *= nums[i]

    post = 1
    for i in reversed(range(len(nums))):
        result[i] *= post
        post *= nums[i]

    return result