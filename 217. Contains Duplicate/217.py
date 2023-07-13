from typing import List

"""
Time Complexity: O(n^2)
Space Complexity: O(1) (no memory needed)
"""
class Naive:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

# Sorting Solution
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass


# Hash Set Solution
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass


# Examples
solutions = [Naive()]

def assert_solutions(nums, output):
    for solution in solutions: 
        assert solution.containsDuplicate(nums) == output

def test_example_1():
    nums = [1,2,3,1]
    output = True

    assert_solutions(nums, output)

def test_example_2():
    nums = [1,2,3,4]
    output = False
    
    assert_solutions(nums, output)

def test_example_3():
    nums = [1,1,1,3,3,4,3,2,4,2]
    output = True

    assert_solutions(nums, output)
