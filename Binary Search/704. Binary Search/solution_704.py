from typing import List


# def index(nums: List[int], target: int) -> int:
#     i = (len(nums)-1)//2

#     while True:
#         if nums[i] > target:
#             newI = (len(nums[:i])-1)//2
#             if newI == i:
#                 return -1
#             i = (len(nums[:i])-1)//2
#         elif nums[i] < target:
#             newI = (len(nums[i:])-1)//2
#             if newI == i:
#                 return -1
#             i = (len(nums[i:])-1)//2
#         else:
#             return i


# def recursive(nums: List[int], target: int) -> int:
#     i = ((len(nums)-1) + 2 // 2) // 2

#     if len(nums) == 0:
#         return -1
#     elif nums[i] == target:
#         if len(nums) == 1:
#             return 1
#         else:
#             return i
#     elif nums[i] > target:
#         result = recursive(nums[:i], target)
#         if (result == -1):
#             return -1
#         return i-result
#     elif nums[i] < target:
#         result = recursive(nums[i+1:], target)
#         if (result == -1):
#             return -1
#         return i+result

#     return -1

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
            r -= 1
        elif nums[m] < target:
            l += 1
        else:
            return m

    return -1
