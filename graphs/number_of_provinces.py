"""
Leetcode 547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""
import collections
from typing import List
from typing import FrozenSet

class Solution:
    # using dfs 98 %
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for i in range(len(isConnected))]
        provinces = 0

        def dfs(matrix: List[List[int]], visited: List[int], row: int):
            for col in range(len(matrix)):
                if matrix[row][col] == 1 and visited[col] == 0:
                    visited[col] = 1
                    dfs(matrix, visited, col)

        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(isConnected, visited, i)
                provinces += 1
        return provinces

class Solution1:
    # using bfs 22.24 %
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        q = []
        for i in range(len(isConnected)):
            if i not in visited:
                q.append(i)
                while q:
                    node = q.pop()
                    visited.add(node)
                    for j in range(len(isConnected)):
                        if isConnected[node][j] == 1 and j not in visited:
                            q.append(j)
                provinces += 1
        return provinces

from collections import deque

class Solution2:
    # using bfs with visited list 74.9%
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0
        q = deque()
        for i in range(n):
            if not visited[i]:
                provinces += 1
                q.append(i)
                while q:
                    x = q.popleft()
                    for y in range(n):
                        if not visited[y] and isConnected[x][y] == 1:
                            visited[y] = 1
                            q.append(y)
        return provinces



class Solution3:
    # using quick union
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]

        def find(i):
            while root[i] != i:
                i = root[i]
            return i

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                root[root_i] = root_j

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    union(i,j)
        provinces = 0
        for idx, i in enumerate(root):
            if idx == i:
                provinces += 1
        return provinces


class Solution4:
    # with path compression
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]

        def find(i):
            while root[i] != i:
                root[i] = root[root[i]]
                i = root[i]
            return i

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                root[root_i] = root_j

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    union(i,j)
        provinces = 0
        for idx, i in enumerate(root):
            if idx == i:
                provinces += 1
        return provinces


class Solution5:
    # with weighted quick union
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]

        def find(i):
            while root[i] != i:
                i = root[i]
            return i

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if rank[p] < rank[q]:
                root[root_p] = root_q
                rank[root_q] += rank[root_p]
            else:
                root[root_q] = root_p
                rank[root_p] += rank[root_q]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    union(i,j)
        provinces = 0
        for idx, i in enumerate(root):
            if idx == i:
                provinces += 1
        return provinces

class Solution6:
    # with weighted quick union with path compression
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]

        def find(i):
            while root[i] != i:
                root[i] = root[root[i]]
                i = root[i]
            return i

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if rank[p] < rank[q]:
                root[root_p] = root_q
                rank[root_q] += rank[root_p]
            else:
                root[root_q] = root_p
                rank[root_p] += rank[root_q]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    union(i,j)
        provinces = 0
        for idx, i in enumerate(root):
            if idx == i:
                provinces += 1
        return provinces


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))
print(Solution1().findCircleNum(isConnected))
print(Solution2().findCircleNum(isConnected))
print(Solution3().findCircleNum(isConnected))
print(Solution4().findCircleNum(isConnected))
print(Solution5().findCircleNum(isConnected))
print(Solution6().findCircleNum(isConnected))

isConnected = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
print(Solution().findCircleNum(isConnected))
print(Solution1().findCircleNum(isConnected))
print(Solution2().findCircleNum(isConnected))
print(Solution3().findCircleNum(isConnected))
print(Solution4().findCircleNum(isConnected))
print(Solution5().findCircleNum(isConnected))
print(Solution6().findCircleNum(isConnected))



