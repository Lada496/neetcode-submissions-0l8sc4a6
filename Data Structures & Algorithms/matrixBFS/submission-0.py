class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        visit.add((0, 0))
        q.append((0, 0))
        
        

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                    
                for dr, dc in DIRS:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                
            length += 1
            

        return -1

        


        