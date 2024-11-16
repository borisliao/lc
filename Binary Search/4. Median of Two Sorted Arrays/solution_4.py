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


def review5(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-19-24
    O(log(n+m))
    """
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2

    l = 0
    r = len(A) - 1

    while True:
        i = (l+r)//2  # s1 /
        j = half-i-2

        aLeft = A[i] if i >= 0 else float('-inf')  # d2 j
        bLeft = B[j] if j >= 0 else float('-inf')
        aRight = A[i+1] if i+1 < len(A) else float('inf')
        bRight = B[j+1] if j+1 < len(B) else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)  # s2 min(aLeft, bLeft)
            return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        elif aLeft > bRight:
            r = i - 1
        else:
            l = i + 1


def review6(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 1-19-24
    Time: 45 min
    Used: Debugger 2
    O(log(n+m))
    """
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A

    total = len(A)+len(B)
    half = total // 2
    l = 0
    r = len(A) - 1

    while True:
        m = (l+r)//2
        n = half-m-2

        aLeft = A[m] if m >= 0 else float('-inf')
        aRight = A[m+1] if m + 1 < len(A) else float('inf')  # d1 + 1
        bLeft = B[n] if n >= 0 else float('-inf')
        bRight = B[n+1] if n + 1 < len(B) else float('inf')  # d1 + 1

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            # d2 min(aLeft, bLeft) + max(aRight, bRight)
            return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        elif aLeft > bRight:
            r = m - 1
        else:
            l = m + 1


def review7(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 2-4-24
    Time: 17 min
    Used: Solution 6
    """
    A, B = nums1, nums2
    if len(A) > len(B):  # s4 >
        A, B = B, A

    total = len(A) + len(B)
    mid = total // 2
    l = 0
    r = len(A) - 1  # s5 len(A)

    while True:  # s6 <
        i = (l + r) // 2
        j = mid - 2 - i  # s3 + i

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i+1] if i + 1 < len(A) else float('inf')  # s2 A[i]
        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j+1] if j + 1 < len(B) else float('inf')  # s2 B[j]

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        elif aLeft > bRight:
            r = i - 1  # s1 swap
        else:
            l = i + 1  # s1 swap


def review8(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 2-5-24
    Time: 12 min
    """
    A, B = nums1, nums2
    if len(A) > len(B):  # s3 >
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2
    l = 0
    r = len(A) - 1

    while True:
        i = (l+r)//2
        j = half-2-i

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i+1] if i+1 < len(A) else float('inf')
        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j+1] if j+1 < len(B) else float('inf')  # s2 j+1 >= 0

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)  # s1 max
            return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        elif aLeft > bRight:
            r = i - 1
        else:
            l = i + 1


def review9(nums1: list[int], nums2: list[int]) -> float:
    """
    Anki 2-5-24
    """
    A, B = nums1, nums2

    if len(A) > len(B):  # s1 >
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2
    l = 0
    r = len(A)-1

    while True:
        i = (l+r)//2
        j = half-2-i

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i+1] if i+1 < len(A) else float('inf')
        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j+1] if j+1 < len(B) else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            else:
                return (max(aLeft, bLeft) + min(aRight, bRight))/2
        if aLeft > bRight:
            r = i - 1
        else:
            l = i + 1


def review10(nums1: list[int], nums2: list[int]) -> float:
    """
    Mochi 4-9-24
    Time: 1 hour
    """
    A, B = nums1, nums2

    if len(nums1) > len(nums2):
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2

    l = 0
    r = len(A) - 1
    while True:
        i = (l+r)//2
        j = half - 2 - i

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i+1] if i < len(A) - 1 else float('inf')
        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j+1] if j+1 < len(B) else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:  # odd
                # right because half interger divided by 2 (rounded down)
                return min(aRight, bRight)
            else:
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        elif aLeft > bRight:
            r = i - 1
        else:
            l = i + 1


def review11(nums1: list[int], nums2: list[int]) -> float:
    """
    Mochi 10-26-24
    """
    A, B = nums1, nums2

    if len(A) > len(B):
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2
    l = 0
    r = len(A)-1

    while True:
        i = (l+r)//2
        j = half-2-i

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i+1] if i+1 < len(A) else float('inf')
        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j+1] if j+1 < len(B) else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            else:
                return (max(aLeft, bLeft) + min(aRight, bRight))/2
        if aLeft > bRight:
            r = i-1
        else:
            l = i+1


def review12(nums1: list[int], nums2: list[int]) -> float:
    """
    Mochi 11-15-24
    """
    nums1, nums2 = nums2, nums1 if len(nums1) > len(nums2) else nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    l = 0
    r = len(nums1) - 1

    while True:
        i = (l+r)//2
        j = half-2-i

        aLeft = nums1[i] if i >= 0 else float('-inf')
        aRight = nums1[i+1] if i < len(nums1)-1 else float('inf')
        bLeft = nums2[j] if j >= 0 else float('-inf')
        bRight = nums2[j+1] if j < len(nums2)-1 else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            else:
                return (max(aLeft, bLeft) + min(aRight, bRight))/2

        if aLeft > bRight:
            r = i-1
        else:
            l = i+1
