class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        dist = 0

        def addroom(r,c):
            if r<0 or r>=ROW or c<0 or c>=COL or (r,c) in visited or grid[r][c] == -1:
                return 

            queue.append((r,c))
            visited.add((r,c))


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        

        while queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
                visited.add((r,c))
                grid[r][c] = dist

                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r, c-1)

            dist+=1

