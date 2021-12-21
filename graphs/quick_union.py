"""
Quick Union Algorithm (Lazy approach)

Find: check if p and q has same root

Union: to merge components containing  p and q set the id of p's root to the id of q's root

NOTE: Quick Union is More efficient than Quick Find because only in the worst case the complexity would O(N^2)


Union-find Constructor	Find	Union	Connected
O(N)	              O(N)  	O(N)	O(N)

"""

class QuickUnionUF:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.N = N
    
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
        self.root[root_p] = root_q
         
        


g = QuickUnionUF(10)
g.union(4, 3)
print(g.root) 
g.union(3, 8)
print(g.root)
g.union(6, 5)
print(g.root)
g.union(9, 4)
print(g.root)
g.union(2, 1)
print(g.root)
print(g.connected(8, 9))
print(g.connected(5, 0))
g.union(5, 0)
print(g.connected(5, 0)) 
g.union(6, 1)


