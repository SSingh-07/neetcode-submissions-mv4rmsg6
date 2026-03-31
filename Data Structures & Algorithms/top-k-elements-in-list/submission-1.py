from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = Counter(nums)
        temp = [(-1*check[k],k) for k in check]     
        heapq.heapify(temp)
        res=[]
        for i in range(0,k):
            res.append((heapq.heappop(temp))[1])

        return res


        