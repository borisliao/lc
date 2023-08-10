from typing import List


def naive(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
def complement(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        idealNumber = target - nums[i]  
        for j in range(len(nums)):
            if i != j:
                if nums[j] == idealNumber:
                    return [i, j]
                
def doubleItterate(nums: List[int], target: int) -> List[int]:
        indexArray = {}

        for i in range(len(nums)):
            indexArray[nums[i]] = i

        for i in range(len(nums)):
            ideal_number = target - nums[i]
            if ideal_number in indexArray:
                if i != indexArray[ideal_number]:
                    return [i, indexArray[ideal_number]]
                
def twoSum(nums: List[int], target: int) -> List[int]:
    """Hashmap and complement"""
    indexArray = {}

    for i in range(len(nums)):
        ideal_number = target - nums[i]
        if ideal_number in indexArray:
            if i != indexArray[ideal_number]:
                return [i, indexArray[ideal_number]]
        indexArray[nums[i]] = i