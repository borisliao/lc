from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True

# Examples
solution = Solution()

def test_example_1():
    nums = [1,2,3,1]
    output = True

    assert solution.containsDuplicate(nums) == output

def test_example_2():
    nums = [1,2,3,4]
    output = False
    
    assert solution.containsDuplicate(nums) == output

def test_example_3():
    nums = [1,1,1,3,3,4,3,2,4,2]
    output = True
    
    assert solution.containsDuplicate(nums) == output
