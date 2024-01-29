# 0000_BFS_TREE.py

# ==============================================================================
# Description
# ==============================================================================
'''
Given a binary tree, return the level order traversal of its nodes' values.
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: TreeNode root
# Output: List[List[int]] 
# Time Complexity: O(n) 
# Space Complexity: O(n) 

# ==============================================================================
# solution
# ==============================================================================
'''
BFS, using a queue to store nodes at each level. Remember to check for the 
length of the queue before looping through it.
'''

# ==============================================================================
# code
# ==============================================================================
from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def bfs_tree(root: Optional[TreeNode])->List[List[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        l = len(q)
        temp_res = []
        for _ in range(l):
            node = q.popleft()
            temp_res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(temp_res)

    return res

# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(bfs_tree(root), [[1]], "Failed on tree with single node.")
    
    def test_complete_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        expected_output = [[1], [2, 3], [4, 5, 6, 7]]
        self.assertEqual(bfs_tree(root), expected_output, "Failed on complete binary tree.")
    
    def test_imbalanced_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected_output = [[1], [2], [3]]
        self.assertEqual(bfs_tree(root), expected_output, "Failed on right-skewed tree.")
    
    def test_empty_tree(self):
        self.assertEqual(bfs_tree(None), [], "Failed on empty tree.")
    
    def test_tree_with_null_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(5)
        expected_output = [[1], [2, 3], [4, 5]]
        self.assertEqual(bfs_tree(root), expected_output, "Failed on tree with null nodes.")

if __name__ == '__main__':
    unittest.main()

