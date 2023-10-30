from typing import List
from collections import defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    mapList = defaultdict(lambda: 0)
    for num in nums:
        mapList[num] +=1
    
    k_val = []
    for key, val in sorted(mapList.items(), key=lambda item: item[1], reverse=True):
        if k == 0:
            break
        k_val.append(key)
        k-=1
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
