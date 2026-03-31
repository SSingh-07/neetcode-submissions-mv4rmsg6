class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        memo = dict()
        LIP =0

        def dfs(r,c, prev):
            if 0<=r<ROW and 0<=c<COL and matrix[r][c]>prev:
                if (r,c) in memo:
                    return memo[(r,c)]

                res = 1
                res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
                res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
                res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
                res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
                memo[(r,c)]=res
                return res

            else:
                return 0

        
        for r in range(ROW):
            for c in range(COL):
                LIP = max(LIP, dfs(r,c,-1))


        return LIP
        