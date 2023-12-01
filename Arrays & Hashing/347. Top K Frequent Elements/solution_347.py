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
