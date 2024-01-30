# 0000_TopologicalSorting.py.py

# ==============================================================================
# Description
# ==============================================================================
'''
Given an adjacency list of a graph, and the number of nodes, return the 
topological sorting of the graph. 
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: adjacency list of graph G, List[List[int]], and number of nodes, int
# Output: List[int] 
# Time Complexity: 
# Space Complexity: 

# ==============================================================================
# solution
# ==============================================================================
'''
The topological sorting consists of adjaceny list, and a list of indegrees. We 
first construct the graph from the adjacency list, then use BFS to traverse the 
graph and update the indegrees. Every time we visit a node, we decrement the 
indegree of its neighbors. When the indegree of a node becomes 0, we add it to 
the queue. 
'''

# ==============================================================================
# code
# ==============================================================================
from typing import List
from collections import defaultdict, deque
def topological_sorting(adj_list: List[List[int]], n: int)->List[int]:
    indegrees = [0] * n
    adj_dict = defaultdict(list)
    for edge in adj_list:
        source = edge[0]
        target = edge[1]
        indegrees[target] += 1
        adj_dict[source].append(target)

    q = deque([])
    for i, indegree in enumerate(indegrees):
        if indegree == 0:
            q.append(i)
            

    res = []
    node_processed = 0
    while q:
        node = q.popleft()
        res.append(node)
        node_processed += 1
        for nei in adj_dict[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    
    if n != node_processed:
        return []
    return res



# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_simple_dag(self):
        adj_list = [[0, 1], [1, 2], [2, 3]]
        n = 4
        expected_output = [0, 1, 2, 3]
        result = topological_sorting(adj_list, n)
        self.assertEqual(result, expected_output)

    def test_multiple_valid_sorts(self):
        adj_list = [[0, 1], [0, 2], [1, 3], [2, 3]]
        n = 4
        result = topological_sorting(adj_list, n)
        self.assertTrue(result in ([0, 1, 2, 3], [0, 2, 1, 3]))

    def test_graph_with_cycle(self):
        adj_list = [[0, 1], [1, 2], [2, 0]]
        n = 3
        result = topological_sorting(adj_list, n)
        self.assertEqual(result, [])  # Assuming your function returns [] for cycles

    def test_unconnected_graph(self):
        adj_list = [[0, 1], [2, 3]]
        n = 4
        result = topological_sorting(adj_list, n)
        self.assertEqual(set(result), set([0, 1, 2, 3]))
        self.assertEqual(len(result), 4)

    def test_single_node(self):
        adj_list = []
        n = 1
        expected_output = [0]
        result = topological_sorting(adj_list, n)
        self.assertEqual(result, expected_output)

    def test_empty_graph(self):
        adj_list = []
        n = 0
        expected_output = []
        result = topological_sorting(adj_list, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

