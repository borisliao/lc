def threeSum(nums: list[int]) -> list[list[int]]:
    """
    12-25-23
    Used: [3Sum - Leetcode 15 - Python](https://www.youtube.com/watch?v=jzZsG8n2R9A)
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        l = i + 1  # d1, cant have repeating characters
        r = len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:  # s2
            continue  # s2

        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue
            if nums[i] + nums[l] + nums[r] == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1  # s3
                r -= 1  # s3
                while nums[l] == nums[l - 1] and l < r:  # s3
                    l += 1  # s3
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1

    return result
