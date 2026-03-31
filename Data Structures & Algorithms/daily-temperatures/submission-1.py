class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        check = []
        for i, j in enumerate(temperatures):
            while check and check[-1][1] < j:
                index, val = check.pop()
                res[index] = i-index

            check.append([i,j])
        return res

        

        