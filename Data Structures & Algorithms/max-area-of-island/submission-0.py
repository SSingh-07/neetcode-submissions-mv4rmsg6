class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        max_size = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                r, c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr< row and 0<=nc<col and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    start = len(visited)
                    bfs(r,c)
                    end = len(visited)
                    max_size = max(max_size, end-start)

        return max_size
                    
        
        