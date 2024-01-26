from collections import defaultdict
from typing import List


def online_solution_abdullayevakbar0101(nums: List[int]) -> int:
    """
    ✅Python3 || C++|| Java✅\[Intervals,Greedy and DP\] without any sort

    Let's break down the code and its logic in more detail:

    1. `std::unordered_map<int, std::pair<int, int>> mp;`

    - `mp` is an unordered map used to store intervals (ranges) of consecutive numbers. Each key represents the right endpoint of an interval, and the corresponding value is a pair `(r, l)` where `r` is the right endpoint and `l` is the left endpoint of the interval.

    2. `std::unordered_map<int, bool> bl;`

    - `bl` is an unordered map used to keep track of whether an element `i` has been visited. If an element has been visited, its corresponding value in this map will be `true;` otherwise, it will be `false.`

    3. `int mx = 0;`

    - `mx` is a variable that keeps track of the maximum length of consecutive sequence found.

    4. The main loop iterates through each element `i` in the input `nums` array.  
        Inside the loop:

        a. `if (bl[i]) { continue; }`  
            If the current element `i` has already been visited, skip it and continue to the next iteration of the loop.  

        b. `bl[i] = true;`  
            Mark the current element `i` as visited by setting its corresponding value in the `bl` map to `true`.  

        c. Initialize `l` and `r` to the current element `i`, representing the left and right endpoints of the current interval.

        d. Check if there is an interval with the right endpoint `i + 1` in the `mp` map using `mp.find(i + 1)`. If such an interval exists, update the right endpoint `r` to the right endpoint of that interval.

        e. Similarly, check if there is an interval with the right endpoint `i - 1` in the `mp` map using `mp.find(i - 1)`. If such an interval exists, update the left endpoint `l` to the left endpoint of that interval.  

        f. Update the `mp` map:  
            Set `mp[r]` to a pair `(r, l)`, indicating the interval with right endpoint `r` and left endpoint l.  
            Set `mp[l]` to the same pair `(r, l)`.  

        g. Calculate the length of the current consecutive sequence as `r - l + 1` and update the maximum length `mx` if this length is greater than the current maximum.

    5. Finally, return the maximum length mx, which represents the length of the longest consecutive sequence found in the input array.

    Explanation from chatgpt. The solution is from me 😇.
    """
    mp = defaultdict(list)
    bl = defaultdict(bool)
    mx = 0
    for i in nums:
        if bl[i]:
            continue
        bl[i] = True
        l, r = i, i
        if mp[i+1]:
            r = mp[i+1][0]
        if mp[i-1]:
            l = mp[i-1][1]
        mp[r] = [r, l]
        mp[l] = [r, l]
        mx = max(mx, r-l+1)
    return mx


def review1(nums: List[int]) -> int:
    """
    Anki review 10/18/23
    https://www.youtube.com/watch?v=P6RZZMu_maU
    """

    numshash = set(nums)

    leng = 0

    for num in numshash:
        if num-1 not in numshash:
            running_total = 0

            while running_total+num in numshash:
                running_total += 1
            leng = max(running_total, leng)

    return leng


def review2(nums: List[int]) -> int:
    """
    Anki 11-12-23
    Debug after running (1)
    Time: 30 min
    """
    num_set = set(nums)

    l = 0
    for n in nums:
        if n-1 not in num_set:  # check if number is start of the sequence
            n_sequence_length = 0

            while n + n_sequence_length in num_set:
                n_sequence_length += 1
            l = max(l, n_sequence_length)

    return l


def review3(nums: List[int]) -> int:
    """
    Anki 11-28-23
    Time: 13:49
    """
    nums = set(nums)

    longest_sequence = 0
    for n in nums:
        if n-1 not in nums:
            current_sequence = 0
            c = n
            while c in nums:
                current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)
                c += 1

    return longest_sequence


def review4(nums: list[int]) -> int:
    """
    Anki 1-26-24
    Time: 10 min
    Used: Debugger 1
    """
    nums = set(nums)
    max_seq = 0

    for n in nums:
        if n-1 in nums:
            continue
        seq = 0  # d1 s did not account for negative numbers
        while n+seq in nums:  # d1 s+1
            seq += 1  # d1 s+=1
            max_seq = max(max_seq, seq)  # d1 s-n
    return max_seq


# def review5(nums: list[int]) -> int:
#     """
#     Anki 1-26-24
#     Time: 10 min
#     Used: Debugger 1
#     """
