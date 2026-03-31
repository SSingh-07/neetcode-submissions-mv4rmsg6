class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh+=1

                elif grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()
                
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh-=1

            time+=1

        return time if fresh==0 else -1

        