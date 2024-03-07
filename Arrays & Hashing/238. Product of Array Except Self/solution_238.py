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


def review3(nums: List[int]) -> List[int]:
    """Anki Reviewed 10/29/23"""
    result = []

    left_products = 1
    for n in nums:
        result.append(left_products)
        left_products *= n

    index = -1
    right_products = 1
    for n in reversed(nums):
        result[index] *= right_products
        right_products *= n
        index -= 1

    return result


def review4(nums: List[int]) -> List[int]:
    """
    Anki 11-12-23
    Used: Whiteboard, Debugger (2)
    """
    l_sums = []
    sum = 1
    for n in nums:
        sum *= n
        l_sums.append(sum)
    l_sums = l_sums[:-1]

    r_sums = []
    sum = 1
    for n in reversed(nums):
        sum *= n
        r_sums.append(sum)
    r_sums = r_sums[:-1]

    result = r_sums[::-1]
    result.append(1)

    i = 1
    for s in l_sums:
        result[i] *= s
        i += 1

    return result


def review5(nums: List[int]) -> List[int]:
    """
    Anki 11-12-23
    Solution recalled from memory
    """
    result = []

    l_sum = 1
    for n in nums:
        result.append(l_sum)
        l_sum *= n

    r_sum = 1
    i = -1
    for n in reversed(nums):
        result[i] *= r_sum
        r_sum *= n
        i -= 1

    return result


def review6(nums: List[int]) -> List[int]:
    """
    Anki 11-16-23
    Used: debugger (1)
    Time: 6m 10s
    """
    result = []

    left = 1
    for n in nums:
        result.append(left)
        left *= n

    index = -1
    right = 1
    for n in reversed(nums):
        result[index] *= right
        right *= n
        index -= 1  # debugger (1)

    return result


def review7(nums: List[int]) -> List[int]:
    """
    Anki 11-16-23
    Used: debugger (1)
    Time: 3:47
    """
    result = []

    left_product = 1
    for n in nums:
        result.append(left_product)
        left_product *= n

    right_product = 1
    i = -1
    for n in reversed(nums):
        result[i] *= right_product
        right_product *= n  # 1d
        i -= 1

    return result


def review7(nums: List[int]) -> List[int]:
    """
    Anki 1-1-24
    Time: 30 min
    Used: debugger 3
    """
    result = []
    product = 1
    for n in nums:
        result.append(product)
        product *= n  # d1 nums product *= nums

    product = 1
    i = len(result) - 1  # d2 i = 0
    for n in reversed(nums):  # d3 result instead of nums
        result[i] *= product
        product *= n
        i -= 1  # d2 i +=1

    return result


def review8(nums: List[int]) -> List[int]:
    """
    Anki 3-7-24
    Time: 11 min
    Used: Solution
    """
    left_sum = []
    t = 1
    for n in nums:
        left_sum.append(t)
        t *= n

    i = len(left_sum) - 1
    t = 1
    for n in reversed(nums):
        left_sum[i] *= t
        t *= n
        i -= 1  # d1

    return left_sum


# def review9(nums: List[int]) -> List[int]:
#     """
#     Anki 3-5-24
#     Time: 11 min
#     Use whiteboard
#     """
