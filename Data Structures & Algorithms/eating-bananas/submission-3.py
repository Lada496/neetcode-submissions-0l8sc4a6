class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = max(piles)
        low, high = 1, total
        res = high

        while low <= high:

            mid = (low + high) // 2
            time = self.hourCounter(piles, mid)

            if time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res

    def hourCounter(self, piles: List[int], rate: int) -> int:
        total = 0
        for pile in piles:
            total += math.ceil(float(pile) / rate)
        
        return total
    


