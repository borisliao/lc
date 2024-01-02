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


def review1(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-28-23
    Used: debugger 3, solution 1
    Time: 53 min
    """
    nums.sort()
    result = []
    for i, n in enumerate(nums):  # d4 n, i
        if i > 0 and nums[i] == nums[i-1]:  # d2
            continue  # d2
        l = i + 1  # s3 + 1
        r = len(nums) - 1
        while l < r:
            total = n + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            elif total == 0:
                result.append([n, nums[l], nums[r]])
                l += 1  # s3
                r -= 1  # s3
                while nums[l] == nums[l - 1] and l < r:  # s3
                    l += 1  # s3

    return result


def review2(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-28-23
    Used: solution 2, [3Sum - Leetcode 15 - Python](https://www.youtube.com/watch?v=jzZsG8n2R9A)
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        l = i+1
        r = len(nums) - 1

        if i > 0 and nums[i] == nums[i-1]:  # s2
            continue  # s2

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:  # s1
                    l += 1  # s1
    return result


def review3(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-28-23
    Time: 14 min
    Used: debugger 3, solution 1
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        l = i + 1  # d3 +1
        r = len(nums) - 1

        # d1 access r before decoration, d3 used nums[r] instead of i, s3 i <= r
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])  # d2 added []
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif total > 0:
                r -= 1
            else:
                l += 1

    return result


def review4(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-31-23
    Time: 15 min
    Used: solution 1, gpt 1
    """
    nums.sort()
    result = []

    for i in range(len(nums)):  # s1 range(nums)
        j = i + 1
        k = len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:  # s1
            continue  # s1

        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:  # gpt2 nums[i] + nums[k] + nums[k]
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif nums[i] + nums[k] + nums[k] > 0:
                k -= 1
            else:
                j += 1

    return result


def review5(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-31-23
    Time: 30 min
    Used: Solution 2
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:  # s2 while i < 0
            continue

        l = i + 1  # s1 + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1

    return result


def review6(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-1-24
    Used: Debugger 2, gpt 1 
    Time: 20 min
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:  # gpt3 nums[i] < nums[i-1]
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_numbers = [nums[i], nums[l], nums[r]]
            if sum(three_numbers) > 0:
                r -= 1  # d2 swapped
            elif sum(three_numbers) < 0:
                l += 1  # d2 swapped
            else:
                result.append(three_numbers)
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return result  # d1


def review7(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-2-24
    Time: 7 min
    Used: solution 1
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:  # s1 while
            continue

        l = i+1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return result
