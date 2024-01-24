# 0001_TwoSum.py

# ==============================================================================
# Description
# ==============================================================================
'''
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: list of integers, target integer
# Output: list of indices
# Time Complexity: O(n)
# Space Complexity: O(n)

# ==============================================================================
# solution
# ==============================================================================
'''
Brute Force:
    Iterate through the list, for each element, iterate through the rest of the
    list to see if the sum is equal to the target. If so, return the indices.
    This would be O(n^2) time complexity and O(1) space complexity.

Better:
    Iterate through the list, for each element, subtract it from the target and
    see if the difference is in the list. If so, return the indices. This would
    be O(n) time complexity and O(n) space complexity.
'''

# ==============================================================================
# code
# ==============================================================================
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         if target - nums[i] in nums[i+1:]:
#             return [i, nums.index(target - nums[i], i+1)]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# ==============================================================================
# test
# ==============================================================================
import unittest

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([0, 4, 3, 0], 0), [0, 3])
        self.assertEqual(two_sum([-1,-2,-3,-4,-5], -8), [2, 4])
    def test_two_sum_empty(self):
        self.assertEqual(two_sum([], 1), None)
    def test_two_sum_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3], 6), None)

if __name__ == '__main__':
    unittest.main()

