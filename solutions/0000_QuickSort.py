# 0000_QuickSort.py

# ==============================================================================
# Description
# ==============================================================================
'''
Implement quick sort algorithm
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: array of integers List[int]
# Output: sorted array List[int] 
# Time Complexity: 
# Space Complexity: 

# ==============================================================================
# solution
# ==============================================================================
'''

'''

# ==============================================================================
# code
# ==============================================================================
from typing import List
def quick_sort(arr: List[int])->List[int]:
    def helper(arr: List[int], start: int, end: int):
        if end <= start:
            return
        left, right = start, end
        pivot = arr[left + (right - left) // 2]
        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        helper(arr, start, right)
        helper(arr, left, end)

    helper(arr, 0, len(arr) - 1)
    return arr
    


# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [], "The sorted list should be empty.")

    def test_single_element(self):
        self.assertEqual(quick_sort([1]), [1], "The sorted list should be [1].")

    def test_repeated_elements(self):
        self.assertEqual(quick_sort([3, 2, 1, 2]), [1, 2, 2, 3], "The sorted list should be [1, 2, 2, 3].")

    def test_negative_numbers(self):
        self.assertEqual(quick_sort([-3, -1, -2, 0]), [-3, -2, -1, 0], "The sorted list should be [-3, -2, -1, 0].")

    def test_regular_case(self):
        self.assertEqual(quick_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5], "The sorted list should be [1, 2, 3, 4, 5].")

    def test_sorted_input(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "The sorted list should be [1, 2, 3, 4, 5].")

    def test_reverse_sorted_input(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "The sorted list should be [1, 2, 3, 4, 5].")

if __name__ == '__main__':
    unittest.main()

