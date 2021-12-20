"""
Quick Find Algorithm (Eager Approach)

Find -> check if both has same ID

Union -> To merge components containing p and q change all entries whose Id equals id[p]  to id[q]

"""


class QuickFindUF:
    def __init__(self, N):
        self.graph = [i for i in range(N)]
        self.N = N
    
    def connected(self, p, q):
        return self.graph[p] == self.graph[q]
    

    def union(self, p, q):
        pid = self.graph[p]
        qid = self.graph[q]
        for i in range(self.N):
            if self.graph[i] == pid:
                self.graph[i] = qid


g = QuickFindUF(10)
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





