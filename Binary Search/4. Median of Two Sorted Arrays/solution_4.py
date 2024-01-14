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
