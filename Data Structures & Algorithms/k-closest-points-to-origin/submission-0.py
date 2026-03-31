class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis =[]
        res1 = []
        for i in points:
            dis.append([math.sqrt((i[0]**2) + (i[1]**2)),i[0],i[1]])

        
        heapq.heapify(dis)
        for i in range(k):
            res1.append(heapq.heappop(dis)[1:])
        return res1
        