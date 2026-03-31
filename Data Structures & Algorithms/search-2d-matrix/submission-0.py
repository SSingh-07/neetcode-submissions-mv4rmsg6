class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = []
        for i in matrix:
            t.extend(i)

        l = 0
        r = len(t) -1

        while l<=r:
            mid = (l + r)//2

            if t[mid] == target:
                return True

            elif t[mid] < target:
                l = mid +1
            
            elif t[mid] > target:
                r = mid -1

        return False

        