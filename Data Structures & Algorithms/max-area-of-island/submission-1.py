class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        visited = set()
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r,c))
            count = 1

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                count += dfs(nr, nc)
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    ans = max(ans, dfs(r, c))
        
        return ans