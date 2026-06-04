class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-st for st in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            
            if second > first:
                heapq.heappush(maxHeap, first - second)

        return abs(maxHeap[0]) if maxHeap else 0

            
