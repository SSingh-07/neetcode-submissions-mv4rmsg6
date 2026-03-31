class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = 0


        def bfs(r, c):
            queue = deque()
            queue.append((r,c))

            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = r+dr, c + dc

                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]=="1" :
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)

                    islands+=1
        return islands
                        


        