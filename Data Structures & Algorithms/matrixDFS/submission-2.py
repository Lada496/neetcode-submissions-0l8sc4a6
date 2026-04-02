class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def counter(x:int,y:int, visited) -> int:
            ROWS, COLS = len(grid), len(grid[0])
            if min(x, y) < 0 or x == ROWS or y == COLS or (x, y) in visited or grid[x][y] == 1:
                return 0
            if x == ROWS - 1 and y == COLS - 1:
                return 1
            
            count = 0
            
            visited.append((x, y))

            count += counter(x - 1, y, visited)
            count += counter(x + 1, y, visited)
            count += counter(x, y - 1, visited)
            count += counter(x, y + 1, visited)

            visited.pop()

            return count
        
        return counter(0,0, [])
        