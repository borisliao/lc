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
