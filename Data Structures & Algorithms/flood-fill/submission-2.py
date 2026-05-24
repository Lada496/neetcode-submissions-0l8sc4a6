class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visited = set()

        def dfs(r, c, origin):
            print(origin)
            if (r, c) in visited or image[r][c] != origin:
                return
            visited.add((r, c))
            
            image[r][c] = color
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr in range(ROWS) and nc in range(COLS):
                    dfs(nr, nc, origin)
        
        dfs(sr, sc, image[sr][sc])
        

        return image
        