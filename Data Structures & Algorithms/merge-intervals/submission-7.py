class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res = []

        for i, j in enumerate(intervals):
            if i!=0:
            
                if j[0] <= res[-1][1]:
                    res[-1][1] = max(j[1], res[-1][1])

                else:
                    res.append(j)

            else:
                res.append(j)

            print(j, res)


        return res
        


        