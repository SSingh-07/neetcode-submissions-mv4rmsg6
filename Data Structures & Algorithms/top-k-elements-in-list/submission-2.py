from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = list((-freq, num) for num, freq in Counter(nums).items())
        heapq.heapify(check)
        return [heapq.heappop(check)[1] for _ in range(k)]
        
        
        