class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        island = 0
        visit = set()

        def bfs(r,c):
            queue= deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r, c = queue.popleft()
                directions=[[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == "1" and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        visit.add((nr,nc))

        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    visit.add((r,c))

                    island+=1
        return island


        