class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(x1**2 + x2**2, x1, x2) for x1, x2 in points]
        heapq.heapify(maxHeap)

        ans = []
        for i in range(k):
            dist, x1, x2 = heapq.heappop(maxHeap)
            ans.append([x1, x2])
        
        return ans
