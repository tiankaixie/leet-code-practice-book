# 0000_Union_Find.py

# ==============================================================================
# Description
# ==============================================================================
'''
You have a graph of `n` nodes. You are given an integer `n` and an array `edges`
where `edges[i] = [ai, bi]`indicates that there is an edge between `ai` and `bi`
in the graph.

Return the number of connected components in the graph.
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: edges: List[List[int]], n: int
# Output: int 
# Time Complexity: 
# Space Complexity: 

# ==============================================================================
# solution
# ==============================================================================
'''
Union find. 
'''

# ==============================================================================
# code
# ==============================================================================
from typing import List
def union_find(edges: List[List[int]], n: int)->int:
    parents = [-1] * n
    def find(i: int)->int:
        if parents[i] == -1:
            return i
        return find(parents[i])

    def union(i: int, j: int):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parents[root_j] = root_i

    for edge in edges:
        i = edge[0]
        j = edge[1]
        union(i, j)

    res = 0
    for i in range(n):
        if parents[i] == -1:
            res +=1

    return res


# ==============================================================================
# test
# =============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_multiple_components(self):
        # Graph with multiple components
        # Component 1: 0-1-2, Component 2: 3-4
        edges = [[0, 1], [1, 2], [3, 4]]
        n = 5
        result = union_find(edges, n)
        self.assertEqual(result, 2, "Expected 2 components")

    def test_single_component(self):
        # Graph with a single component
        # Component: 0-1-2-3
        edges = [[0, 1], [1, 2], [2, 3]]
        n = 4
        result = union_find(edges, n)
        self.assertEqual(result, 1, "Expected 1 component")

    def test_no_edges(self):
        # Graph with no edges, each node is a separate component
        edges = []
        n = 5
        result = union_find(edges, n)
        self.assertEqual(result, 5, "Expected 5 components")

    def test_self_loops(self):
        # Graph with self loops, should be treated as single nodes
        edges = [[0, 0], [1, 1], [2, 2]]
        n = 3
        result = union_find(edges, n)
        self.assertEqual(result, 3, "Expected 3 components")
        
    def test_duplicate_edges(self):
        # Graph with duplicate edges
        edges = [[0, 1], [1, 2], [0, 1], [2, 3], [3, 4], [3, 4]]
        n = 5
        result = union_find(edges, n)
        self.assertEqual(result, 1, "Expected 1 component")

if __name__ == '__main__':
    unittest.main()

