class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        ans = 0
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            ans = w1
            
            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))
        
        if len(visited) == n:
            return ans
        
        return -1
        
    
