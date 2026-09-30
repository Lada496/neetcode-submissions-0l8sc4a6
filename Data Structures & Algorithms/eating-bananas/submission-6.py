class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            
            return total <= h

        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        
        return l
