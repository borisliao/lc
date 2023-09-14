from typing import List


# def attempt1(nums: List[int]) -> int:
#     """using flynns tortise and hare algo"""
#     fast, slow = 0, 0

#     while True:
#         fast = (fast + 2) % len(nums)
#         slow = (slow + 1) % len(nums)

#         if fast != slow and nums[fast] == nums[slow]:
#             return nums[fast]

def attempt2(nums: List[int]) -> int:
    """
    Hint from neetcode: https://www.youtube.com/watch?v=wjYnzkAhcNk
    using flynns tortise and hare algo
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
