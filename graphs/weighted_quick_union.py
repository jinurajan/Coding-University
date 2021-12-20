"""
Weighted Quick Union Algorithm

Find: check if p and q has same root

Union: to merge components containing p and q make the root of the smallest tree to the root of largest tree
       Link root of smaller tree to root of larger tree

Union-find Constructor	Find	Union	 Connected
O(N)	                O(logN)	O(logN)	 O(logN)

"""

class WeightedQuickUnionUF:
    def __init__(self, N):
        self.root= [i for i in range(N)]
        self.rank = [1 for i in range(N)]
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
        if self.rank[p] < self.rank[q]:
            self.root[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        else:
            self.root[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
            
         
        


g = WeightedQuickUnionUF(10)
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


