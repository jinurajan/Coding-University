"""
Quick Union with Path Compression Algorithm

Find: check if p and q has same find

Union: to merge components containing p and q make the find of the smallest tree to the find of largest trees 
       Link find of smaller tree to find of larger tree

Union-find Constructor	Find	  Union	    Connected
O(N)   	                O(log N) O(logN)	O(log N)

"""

class QuickUnionPathCompressionUF:
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
        find_p = self.find(p)
        find_q = self.find(q)
        self.root[find_p] = find_q
            
         
    


g = QuickUnionPathCompressionUF(10)
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


