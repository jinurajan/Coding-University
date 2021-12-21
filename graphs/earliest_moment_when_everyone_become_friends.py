"""
Leetcode 1101. The Earliest Moment When Everyone Become Friends
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.


Solution / Thoughts:

1. undirected graph
2. when all nodes are connected -> return
3. earliest ? start from the sorted timestamp ?
4. dfs start from earliest friendship and then so on until all nodes are connected
"""
from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort the logs by timestamp to start
        logs = sorted(logs, key=lambda x: x[0])
        union_find = UnionFind(n)
        for ts, u, v in logs:
            union_find.union(u, v)
            if union_find.count == n-1:
                return ts
        return -1


class UnionFind:
    def __init__(self, N):
        self.root= [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.N = N
        self.count = 0
    
    def find(self, node):
        while self.root[node] != node:
            node = self.root[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        self.count += 1
        if self.rank[p] < self.rank[q]:
            self.root[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        else:
            self.root[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
print(Solution().earliestAcq(logs, n))

logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
n = 4
print(Solution().earliestAcq(logs, n))
