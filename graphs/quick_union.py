"""
Quick Union Algorithm (Lazy approach)

Find: check if p and q has same root

Union: to merge components containing  p and q set the id of p's root to the id of q's root

"""

class QuickUnionUF:
    def __init__(self, N):
        self.graph = [i for i in range(N)]
        self.N = N
    
    def root(self, node):
        while self.graph[node] != node:
            node = self.graph[node]
        return node

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        self.graph[p] = root_q
         
        


g = QuickUnionUF(10)
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


