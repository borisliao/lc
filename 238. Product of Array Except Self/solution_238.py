from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
        """
        Using Dynamic Programming (DP)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        pre = 1
        post = 1
        output = []

        for i in range(len(nums)):
            output.append(pre)
            if pre != 0 or pre != len(nums):
                pre *= nums[i]

        for i in reversed(range(len(nums))):
            output[i] *= post
            if post != 0 or post != len(nums):
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
