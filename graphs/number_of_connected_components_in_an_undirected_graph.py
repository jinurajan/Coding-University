"""
323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


Solution: dfs and count += 1

union_find and then count the roots


"""
from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    """ Using dfs with recursion
        Best Solution
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjascency_list = defaultdict(list)
        for u, v in edges:
            adjascency_list[u].append(v)
            adjascency_list[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adjascency_list[node]:
                dfs(nei)
            
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count

class Solution1:
    """ Using dfs with iteration
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjascency_list = defaultdict(list)
        for u, v in edges:
            adjascency_list[u].append(v)
            adjascency_list[v].append(u)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                stack = [i]
                while stack:
                    node = stack.pop()
                    for nei in adjascency_list[node]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        stack.append(nei)
                count += 1
        return count


class Solution2:
    """ Using unionfind
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = WeightedPathCompressionQuickUnionUF(n)
        components = n
        for u, v in edges:
            if unionFind.union(u, v):
                components -= 1
        return components

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
edges = [[0,1],[1,2],[3,4]]
print(Solution().countComponents(n, edges))
print(Solution1().countComponents(n, edges))
print(Solution2().countComponents(n, edges))
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print(Solution().countComponents(n, edges))
print(Solution1().countComponents(n, edges))
print(Solution2().countComponents(n, edges))



