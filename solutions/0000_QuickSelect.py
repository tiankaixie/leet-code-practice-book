# 0000_QuickSelect.py

# ==============================================================================
# Description
# ==============================================================================
'''
Find the top K largest elements in an array
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: List[int] arr, int k 
# Output: List[int] 
# Time Complexity: 
# Space Complexity: 

# ==============================================================================
# solution
# ==============================================================================
'''
Quick select. 
'''

# ==============================================================================
# code
# ==============================================================================
from typing import List
def quick_select(arr: List[int], k: int)->List[int]:
    if len(arr) ==0 or k == 0: return []
    if len(arr) < k: return arr
    def helper(arr: List[int], start: int, end: int, k: int):
        left, right = start, end
        pivot = arr[left + (right - left) // 2]
        while left <= right:
            while left <= right and arr[left] > pivot:
                left += 1
            while left <= right and arr[right] < pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return helper(arr, start, right, k)
        if start + k - 1 >= left:
            return helper(arr, left, end, k + start - left)
        return right + 1 

    i =  helper(arr, 0, len(arr) - 1, k)
    return arr[:i+1]

    

# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_regular_case(self):
        self.assertCountEqual(quick_select([3, 2, 1, 5, 6, 4], 2), [6, 5], "Should return the top 2 largest elements.")

    def test_k_equals_array_length(self):
        self.assertCountEqual(quick_select([3, 2, 1], 3), [3, 2, 1], "Should return all elements when k equals the array length.")

    def test_k_greater_than_array_length(self):
        self.assertCountEqual(quick_select([3, 2, 1], 4), [3, 2, 1], "Should return all elements when k is greater than the array length.")

    def test_with_negative_numbers(self):
        self.assertCountEqual(quick_select([3, -2, 1, 5, -6, 4], 2), [5, 4], "Should handle negative numbers correctly.")

    def test_with_duplicates(self):
        self.assertCountEqual(quick_select([4, 4, 4, 4, 4], 2), [4, 4], "Should handle duplicate numbers correctly.")

    def test_empty_array(self):
        self.assertEqual(quick_select([], 2), [], "Should return an empty list when the array is empty.")

    def test_k_is_zero(self):
        self.assertEqual(quick_select([3, 2, 1], 0), [], "Should return an empty list when k is 0.")

if __name__ == '__main__':
    unittest.main()

