class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            preMap[a].append(b)
        visited =set()
        res =[]

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):return False
                else:
                    if pre not in res:
                        res.append(pre)
            res.append(crs)
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return res





        