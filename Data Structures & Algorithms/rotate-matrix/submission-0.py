class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for r in range(N):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for i in matrix:
            i.reverse()


        return matrix
        