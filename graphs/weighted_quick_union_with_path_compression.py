"""
Weighted Quick Union with Path Compression Algorithm

Find: check if p and q has same root

Union: to merge components containing p and q make the root of the smallest tree to the root of largest trees 
       Link root of smaller tree to root of larger tree

"""

class WeightedPathCompressionQuickUnionUF:
    def __init__(self, N):
        self.graph = [i for i in range(N)]
        self.size = [1 for i in range(N)]
        self.N = N
    
    def root(self, node):
        while self.graph[node] != node:
            self.graph[node] = self.graph[self.graph[node]]
            node = self.graph[node]
        return node

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        if root_p == root_q:
            return
        if self.size[p] < self.size[q]:
            self.graph[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.graph[root_q] = root_p
            self.size[root_p] += self.size[root_q]
            
         
        


g = WeightedPathCompressionQuickUnionUF(10)
g.union(4, 3)
print(g.graph) 
g.union(3, 8)
print(g.graph)
g.union(6, 5)
print(g.graph)
g.union(9, 4)
print(g.graph)
g.union(2, 1)
print(g.graph)
print(g.connected(8, 9))
print(g.connected(5, 0))
g.union(5, 0)
print(g.connected(5, 0)) 
g.union(6, 1)


