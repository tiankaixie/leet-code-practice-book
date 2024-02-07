# 0000_MergeThreeSortedArray.py

# ==============================================================================
# Description
# ==============================================================================
'''
You are given three integer arrays nums1, nums2 and nums3, sorted in 
non-decreasing order, and three integers x, y and z representing the number of 
elements in nums1, nums2, and nums3 respectively.

Merge nums1, nums2 and nums3 into a single array sorted in non-decreasing order.
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
import heapq

def merge_sorted_arrays(nums1, nums2, nums3):
    min_heap = []
    result = []
    
    if len(nums1) != 0:   
        heapq.heappush(min_heap, (nums1[0], 0, 0))
    if len(nums2) != 0:
        heapq.heappush(min_heap, (nums2[0], 1, 0))
    if len(nums3) != 0:
        heapq.heappush(min_heap, (nums3[0], 2, 0))
            
    
    # Merge all arrays
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if list_idx == 0 and element_idx + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[element_idx + 1], list_idx, element_idx + 1))
        elif list_idx == 1 and element_idx + 1 < len(nums2):
            heapq.heappush(min_heap, (nums2[element_idx + 1], list_idx, element_idx + 1))
        elif list_idx == 2 and element_idx + 1 < len(nums3):
            heapq.heappush(min_heap, (nums3[element_idx + 1], list_idx, element_idx + 1))
            
    return result


# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_basic(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        nums3 = [0, 7, 8, 9]
        self.assertEqual(merge_sorted_arrays(nums1, nums2, nums3), [0,1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()

