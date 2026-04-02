class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k:int) -> bool:
            count = 0
            for pile in piles:
                count += math.ceil(float(pile) / k)
            
            return count <= h
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low