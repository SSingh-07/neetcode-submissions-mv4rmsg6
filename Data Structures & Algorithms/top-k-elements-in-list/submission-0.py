class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        heapp = []
        result =[]

        for i in data:
            heapp.append((-data[i], i))
        
        heapq.heapify(heapp)

        while k and len(heapp):
            result.append(heapq.heappop(heapp)[1])
            k-=1

        return result
            

        

        