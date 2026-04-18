class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in visited:
                return False
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                dfs(nr, nc)
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # This is the start of a new island!
                    count += 1
                    dfs(r, c) 
        return count
    