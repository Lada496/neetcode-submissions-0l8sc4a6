class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, curComb):
            if len(curComb) == k:
                res.append(curComb.copy())
            if i > n:
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                backtrack(j + 1, curComb)
                curComb.pop()
        
        backtrack(1, [])

        return res