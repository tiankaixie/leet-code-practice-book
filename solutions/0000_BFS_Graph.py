# 0000_BFS_Graph.py

# ==============================================================================
# Description
# ==============================================================================
'''
Given a graph, return the level order traversal of its nodes' values.
'''

# ==============================================================================
# Specifications
# ==============================================================================
# Input: adjacency list of graph G, List[List[int]]
# Output: List[List[int]] 
# Time Complexity: O(V + E + d * klogk) where V is number of nodes, E is number
#                  of edges, d is the maximum of depth of graph, and k is max of
#                  nodes per level.
# Space Complexity: O(V + E + d * klogk) 

# ==============================================================================
# solution
# ==============================================================================
'''
Construct a graph from the adjacency list, then do BFS on the graph.
'''

# ==============================================================================
# code
# ==============================================================================
from typing import List
from collections import defaultdict, deque
class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.adj = {}

def bfs_graph(adj_list: List[List[int]])->List[List[int]]:
    node_dict = {}
    indegree = defaultdict(int) 
    for edge in adj_list:
        source = edge[0]
        target = edge[1]
        if source not in node_dict:
            node_dict[source] = GraphNode(source)
        if target not in node_dict:
            node_dict[target] = GraphNode(target)
        node_dict[source].adj[target] = node_dict[target]
        indegree[target] += 1

    root = None
    for k in node_dict.keys():
        if indegree[k] == 0:
            root = node_dict[k]

    if not root:
        return []
    
    q = deque([root])
    visited = set([root.val])
    res = []
    while q:
        l = len(q)
        temp_res = []
        for _ in range(l):
            node = q.popleft()
            temp_res.append(node.val)
            for nei in node.adj.keys():
                if nei not in visited:
                    q.append(node.adj[nei])
                    visited.add(nei)

        res.append(sorted(temp_res))

    return res
                    



# ==============================================================================
# test
# ==============================================================================
import unittest

class TestThis(unittest.TestCase):
    def test_single_node(self):
        adj_list = [[1, 1]]
        self.assertEqual(bfs_graph(adj_list), [], "Failed on graph with a single node.")
    
    def test_linear_graph(self):
        adj_list = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(bfs_graph(adj_list), [[1], [2], [3], [4]], "Failed on linear graph.")
    
    def test_tree_structure_graph(self):
        adj_list = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]
        self.assertEqual(bfs_graph(adj_list), [[1], [2, 3], [4, 5, 6]], "Failed on tree-structured graph.")
    
    def test_graph_with_cycle(self):
        adj_list = [[1, 2], [2, 3], [3, 1]]
        self.assertEqual(bfs_graph(adj_list), [], "Failed on graph with cycle.")
    
    def test_empty_graph(self):
        adj_list = []
        self.assertEqual(bfs_graph(adj_list), [], "Failed on empty graph.")

if __name__ == '__main__':
    unittest.main()

