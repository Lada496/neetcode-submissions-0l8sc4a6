class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set() # (r, c)
        t = 0

        minHeap = [(grid[0][0], 0, 0)] # weight, r, c

        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if (r, c) == (ROW - 1, COL - 1):
                return max(t, w)
            visited.add((r, c))
            t = max(w, t)
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr < 0 or nr >= ROW or
                    nc < 0 or nc >= COL or
                    (nr, nc) in visited):
                    continue
                
                heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
        
