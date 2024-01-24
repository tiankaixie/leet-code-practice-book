# 0000_BinarySearch.py

# ==============================================================================
# Description
# ==============================================================================
'''
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: 
# Output: 
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
def binary_search(arr, target):
    if len(arr) == 0:
        return None
    left = 0
    right = len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid

    if arr[left] == target:
        return left
    if arr[right] == target:
        return right
    return None
    
# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9,10], 5), 4)
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9,10], 1), 0)
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9,10], 10), 9)
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9,10], 11), None)
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9,10], 0), None)
    def test_binary_search_empty(self):
        self.assertEqual(binary_search([], 5), None)

if __name__ == '__main__':
    unittest.main()

