def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    1-13-24
    Used: [Median of Two Sorted Arrays - Binary Search - Leetcode 4](https://www.youtube.com/watch?v=q6IEA26hvXc)
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


def review1(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-14-24
    Used: Solution 6, gpt 1
    Time: 30 min
    """
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A

    l = 0
    r = len(A) - 1  # s5 - 1
    while True:
        i = (l+r) // 2
        j = (half-2) - i  # s4 total-2

        a_left = A[i] if i >= 0 else float('-inf')  # s6 >
        a_right = A[i+1] if i+1 < len(A) else float('inf')
        b_left = B[j] if j >= 0 else float('-inf')  # s6 >, gpt7
        b_right = B[j+1] if j+1 < len(B) else float('inf')

        if a_left <= b_right and b_left <= a_right:
            if total % 2 == 1:
                return min(a_right, b_right)  # s1 min(a_left,b_right)
            # s2 return (a_left + b_right) / 2
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:  # s3
            r = i - 1  # s3
        else:  # s3
            l = i + 1  # s3


def review2(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-14-24
    Used: solution 4
    Time: 37 min
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A

    l = 0
    r = len(A)-1  # s4 (half-2)-1
    while True:
        i = (l+r)//2
        j = (half-2) - i

        a_left = A[i] if i >= 0 else float('-inf')
        a_right = A[i + 1] if i + 1 < len(A) else float('inf')
        b_left = B[j] if j >= 0 else float('-inf')
        b_right = B[j + 1] if j + 1 < len(B) else float('inf')

        if a_left <= b_right and b_left <= a_right:
            if total % 2 == 1:
                return min(a_right, b_right)  # s1 min(a_left, b_right)
            # s2 (a_left + b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            r = i - 1  # s3 j
        else:
            l = j + 1  # s3 i


def review3(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-18-24
    O(m+n) merged solution
    Time: 20 min
    """
    merged = []
    i, j = 0, 0  # d1 , 0
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
            else:
                merged.append(nums1[i])
                i += 1
        elif i < len(nums1):
            merged.extend(nums1[i:])
            break
        else:
            merged.extend(nums2[j:])
            break

    middle = (len(merged) - 1) // 2

    if len(merged) % 2:  # d2 middle % 2
        return merged[middle]
    else:
        return (merged[middle] + merged[middle+1]) / 2  # d3 parentheses


def review4(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-19-24
    Used: [Median of Two Sorted Arrays - Binary Search - Leetcode 4](https://www.youtube.com/watch?v=q6IEA26hvXc)
    O(log(n+m))
    """
    A, B = nums1, nums2
    if len(A) > len(B):  # s5 <
        A, B = B, A

    total = len(nums1) + len(nums2)
    half = total // 2

    l = 0
    r = len(A) - 1  # s6 len(A)
    while True:
        i = (l+r) // 2
        j = half-i-2

        a_left = A[i] if i >= 0 else float('-inf')  # s7 i < 0
        a_right = A[i+1] if i+1 < len(A) else float('inf')
        b_left = B[j] if j >= 0 else float('-inf')  # s7 i < 0
        b_right = B[j+1] if j+1 < len(B) else float('inf')  # s8  j+1 < 0

        if a_left <= b_right and b_left <= a_right:  # s4 <
            if total % 2:
                return min(a_right, b_right)  # s3 return min(a_left, b_left)
            # s2 min(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            r = i-1  # s1 l += 1
        else:
            l = j+1  # s1 r -= 1


# def review5(nums1: list[int], nums2: list[int]) -> float:
#     """
#     Anki 1-19-24
#     Used: [Median of Two Sorted Arrays - Binary Search - Leetcode 4](https://www.youtube.com/watch?v=q6IEA26hvXc)
#     O(log(n+m))
#     """
