import heapq
from typing import List
from collections import Counter, defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    mapList = defaultdict(lambda: 0)
    for num in nums:
        mapList[num] += 1

    k_val = []
    for key, val in sorted(mapList.items(), key=lambda item: item[1], reverse=True):
        if k == 0:
            break
        k_val.append(key)
        k -= 1
    return k_val


def review1(nums: List[int], k: int) -> List[int]:
    """Anki Reviewed 10/29/23"""
    count = defaultdict(lambda: 0)
    buckets = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] += 1

    for n, frequency in count.items():
        buckets[frequency].append(n)

    index = -1
    result = []
    while len(result) < k:
        if buckets[index]:
            result.append(buckets[index].pop())
        else:
            index -= 1
    return result


def review2(nums: List[int], k: int) -> List[int]:
    """
    Anki 11-14-23
    Used: [heap docs](https://docs.python.org/3/library/heapq.html), [dict docs](https://realpython.com/iterate-through-dictionary-python/#looping-over-dictionary-items-the-items-method)
          debugger (3)
    Time: 28 min
    """
    freq = defaultdict(lambda: 0)

    for n in nums:
        freq[n] += 1

    values = []
    for n, f in freq.items():
        heapq.heappush(values, (f, n))

    return [n for f, n in heapq.nlargest(k, values, lambda x: x[0])]


def review3(nums: List[int], k: int) -> List[int]:
    """
    Anki 11-14-23
    Used: debugger (2)
    Time: 29 min
    """
    nums_dict = defaultdict(lambda: 0)
    for n in nums:
        nums_dict[n] += 1

    bucket = [[] for _ in range(len(nums) + 1)]  # debugger (1)
    for number, frequency in nums_dict.items():
        bucket[frequency].append(number)

    i = -1
    result = []
    while len(result) < k:
        if bucket[i]:
            result.append(bucket[i].pop())
        else:  # debugger (2)
            i -= 1
    return result


def review4(nums: List[int], k: int) -> List[int]:
    """
    Anki 11-17-23
    Used: peak at solution (2), debugger (3)
    Time: 30 min
    """
    count = defaultdict(lambda: 0)
    for n in nums:
        count[n] += 1  # peak at solution (2)

    freq = [[] for _ in range(len(nums) + 1)]
    for n, f in count.items():
        freq[f].append(n)

    result = []
    i = -1
    while len(result) < k:  # debugger (1)
        if freq[i]:  # peak at solution (1)
            result.append(freq[i].pop())  # debugger (2)
        else:  # debugger (3)
            i -= 1
    return result


def review5(nums: List[int], k: int) -> List[int]:
    """
    Anki 11-20-23
    Used: debugger (1)
    Time: 20m15s, whiteboarded
    """
    freq = defaultdict(lambda: 0)
    for n in nums:
        freq[n] += 1

    freq_count = [[] for _ in range(len(nums) + 1)]  # debugger (1)
    for n, count in freq.items():
        freq_count[count].append(n)

    i = -1
    result = []
    while len(result) < k:
        if freq_count[i]:
            result.append(freq_count[i].pop())
        else:
            i -= 1

    return result


def review6(nums: List[int], k: int) -> List[int]:
    """
    Anki 11-30-23
    Used: debugger (1), solution (1)
    Time: 14:15
    """
    number_counts = Counter(nums)

    frequency = [[] for _ in range(len(nums) + 1)]

    for number, count in number_counts.items():
        frequency[count].append(number)

    result = []
    i = -1
    while len(result) < k:
        if frequency[i]:  # d1
            # s2 (frequency[i].pop not frequency.pop)
            result.append(frequency[i].pop())
        else:
            i -= 1

    return result


def review6(nums: List[int], k: int) -> List[int]:
    """
    Anki 12-19-23
    Time: 14:51
    Used: Debugger 1
    """
    count = defaultdict(lambda: 0)
    for n in nums:
        count[n] += 1

    numbers_for_count = defaultdict(lambda: [])
    for n, c in count.items():
        numbers_for_count[c].append(n)

    result = []
    for c in reversed(range(len(nums)+1)):  # d1 range(len(nums)) 0th indexed
        for n in numbers_for_count[c]:
            result.append(n)
            if len(result) == k:
                return result

    return result


def review6(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-26-24
    Time: 16 min
    Used: Debugger 1
    """
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    # d1 [[]]*(len(nums) + 1) shares the same pointer
    occurance = [[] for _ in range((len(nums) + 1))]
    for n, o in count.items():
        occurance[o].append(n)

    result = []
    for li in reversed(occurance):
        for n in reversed(li):
            result.append(n)
            k -= 1
            if k == 0:
                return result


def review7(nums: list[int], k: int) -> list[int]:
    """
    Anki 3-7-24
    Time: 10:44
    Used: solution 2, debugger 1
    """
    count = Counter(nums)

    occ = [[] for _ in range(len(nums)+1)]  # s3 +1

    for n, c in count.items():  # s1 .items()
        occ[c].append(n)  # d2 append[n]``

    result = []
    for l in reversed(occ):
        while l:
            result.append(l.pop())
            k -= 1
            if k == 0:
                return result


def review8(nums: list[int], k: int) -> list[int]:
    """
    Mochi 10-5-24
    """
    count = {}
    # 1: 3
    # 2: 2
    # 3: 1
    for n in nums:  # nums =  [1,1,1,2,2,3]
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    instances = {}
    # 1: [3]
    # 2: [2]
    # 3: [1]
    for n, freq in count.items():  # d1 .items()
        if freq in instances:
            instances[freq].append(n)
        else:
            instances[freq] = [n]

    result = []  # [1, 2]
    for freq in range(len(nums), 0, -1):  # d2 reverse order
        # d3 while loop to keep popping items
        while freq in instances and instances[freq]:
            result.append(instances[freq].pop())
            if len(result) == k:
                return result
