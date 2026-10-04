class UnionFind:
    
    def __init__(self, n: int):
        self.rank = {}
        self.par = {}
        self.num = n

        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
        

    def find(self, x: int) -> int:
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        xp = self.find(x)
        xy = self.find(y)

        return xp == xy


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        
        xp, yp = self.find(x), self.find(y)
        if self.rank[xp] > self.rank[yp]:
            self.par[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.par[xp] = yp
        else:
            self.par[xp] = yp
            self.rank[yp] += 1
        self.num -= 1
        return True
        
        

    def getNumComponents(self) -> int:
        return self.num

