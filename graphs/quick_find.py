"""
Quick Find Algorithm (Eager Approach)

Find -> check if both has same ID

Union -> To merge components containing p and q change all entries whose Id equals id[p]  to id[q]

Union-find Constructor	Find	Union	Connected
O(N) 	                O(1) 	O(N)	O(1)

"""


class QuickFindUF:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.N = N
    
    def connected(self, p, q):
        return self.root[p] == self.root[q]

    def union(self, p, q):
        pid = self.root[p]
        qid = self.root[q]
        if pid == qid:
            return
        for i in range(self.N):
            if self.root[i] == pid:
                self.root[i] = qid


g = QuickFindUF(10)
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





