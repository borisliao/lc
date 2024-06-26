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


def review8(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-8-24
    Used: solution 2
    Time: 14 min
    """
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:  # s1
            continue  # s1

        l = i + 1
        r = len(nums) - 1

        while l < r:
            values = [nums[i], nums[l], nums[r]]
            if sum(values) == 0:
                result.append(values)
                l += 1  # s2
                while l < r and nums[l] == nums[l-1]:  # s2
                    l += 1  # s2
            elif sum(values) > 0:
                r -= 1
            else:
                l += 1

    return result


def review9(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-17-24
    Time: 19 min
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        l = i+1
        r = len(nums) - 1
        while l < r:
            target = nums[i] + nums[l] + nums[r]
            if target == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l-1] == nums[l]:
                    l += 1
            elif target > 0:
                r -= 1
            else:
                l += 1

    return result


def review10(nums: list[int]) -> list[list[int]]:
    """
    Mochi 4-8-24
    Time: 25 min
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:  # s1
            continue  # s1

        l = i+1  # d2
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] + nums[i] == 0:
                # d4 result.append([l, i, r])
                result.append([nums[i], nums[l], nums[r]])
                l += 1  # d3
                while l < r and nums[l-1] == nums[l]:  # d3
                    l += 1  # d3
            elif nums[l] + nums[r] + nums[i] > 0:
                r -= 1
            else:
                l += 1
    return result


# def review11(nums: list[int]) -> list[list[int]]:
#     """
#     Mochi 6-26-24
#     """
#     nums.sort()

#     subset = []
#     result = []

#     def dfs(i):
#         if sum(subset) == 0:
#             result.append(subset.copy())
#             return
#         if i >= len(nums):
#             return

#         subset.append(nums[i])
#         dfs(i+1)
#         subset.pop()
#         i += 1
#         while i >= len(nums) and nums[i-1] == nums[i]:
#             i += 1
#         dfs(i)

#     dfs(0)
#     return result
