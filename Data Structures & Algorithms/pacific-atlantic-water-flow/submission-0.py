class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pcf, atl = set(), set()
        res =[]

        def dfs(r, c, visit, prev):
            if 0<=r<ROW and 0<=c<COL and (r,c) not in visit and heights[r][c] >= prev:
                visit.add((r,c))
                dfs(r+1, c, visit, heights[r][c])
                dfs(r-1, c, visit, heights[r][c])
                dfs(r, c+1, visit, heights[r][c])
                dfs(r, c-1, visit, heights[r][c])

        for c in range(COL):
            dfs(0,c,pcf,heights[0][c])
            dfs(ROW-1,c,atl,heights[ROW-1][c])

        for r in range(ROW):
            dfs(r,0,pcf,heights[r][0])
            dfs(r,COL-1,atl,heights[r][COL-1])

        for r,c in pcf:
            if (r,c) in atl:
                res.append((r,c))

        return res


        