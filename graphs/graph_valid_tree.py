"""
261. Graph Valid Tree: https://leetcode.com/problems/graph-valid-tree/solution/

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


Solution: A graph is a tree when there is only one root for all nodes and all nodes are connected

"""
from typing import List
from collections import defaultdict 
from collections import deque

class Solution:
    """
    Using dfs with adjascency list format recursion

    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjascency_list = defaultdict(list)
        for u, v in edges:
            adjascency_list[u].append(v)
            adjascency_list[v].append(u)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adjascency_list[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                result = dfs(nei, node)
                if not result:
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

class Solution1:
    """
    Using dfs with adjascency list format

    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjascency_list = defaultdict(list)
        for u, v in edges:
            adjascency_list[u].append(v)
            adjascency_list[v].append(u)
        
        stack = deque([0])
        # create a parent map instead of visited
        parent = {0: -1}
        while stack:
            node = stack.pop()
            for nei in adjascency_list[node]:
                if parent.get(node) == nei:
                    continue
                if parent.get(nei):
                    return False
                stack.append(nei)
                parent[nei] = node
        return len(parent) == n

class Solution2:
    """
    Using dfs with adjascency list format
    # legacy dfs pattern wont work for undirected graphs hence
    DO NOT USE THIS FUNCTION

    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjascency_list = defaultdict(list)
        for u, v in edges:
            adjascency_list[u].append(v)
            adjascency_list[v].append(u)
        
        stack = deque([0])
        visited = {0}
        while stack:
            node = stack.pop()
            for nei in adjascency_list[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                stack.append(nei)
                adjascency_list.get(nei).remove(node)
        return len(visited) == n 
            

class Solution3:
    """
    Using Weighted Quick Union with path compression
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        unionFind = WeightedPathCompressionQuickUnionUF(n)
        for u, v in edges:
            if not unionFind.union(u, v):
                return False
        return True
        
class WeightedPathCompressionQuickUnionUF:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.N = N
    
    def find(self, node):
        while self.root[node] != node:
            self.root[node] = self.root[self.root[node]]
            node = self.root[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return False
        if self.rank[p] < self.rank[q]:
            self.root[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        else:
            self.root[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        return True
        
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(Solution().validTree(n, edges))
print(Solution1().validTree(n, edges))
print(Solution2().validTree(n, edges))
print(Solution3().validTree(n, edges))
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(Solution().validTree(n, edges))
print(Solution1().validTree(n, edges))
print(Solution2().validTree(n, edges))
print(Solution3().validTree(n, edges))
n = 4
edges = [[0,1],[2,3]]
print(Solution().validTree(n, edges))
print(Solution1().validTree(n, edges))
print(Solution2().validTree(n, edges))
print(Solution3().validTree(n, edges))
n = 2
edges = [[1,0]]
print(Solution().validTree(n, edges))
print(Solution1().validTree(n, edges))
print(Solution2().validTree(n, edges))
print(Solution3().validTree(n, edges))
