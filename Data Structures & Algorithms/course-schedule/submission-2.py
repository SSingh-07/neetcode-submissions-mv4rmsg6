class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {crs:[] for crs in range(numCourses)}
        for crs, req in prerequisites:
            preMap[crs].append(req)

        visited= set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)
            for c in preMap[crs]:
                if not dfs(c): return False

            visited.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c): return False

        return True
        