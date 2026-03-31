class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        myheap = nums[:k]
        heapq.heapify(myheap)

        for i in nums[k:]:
            if i > myheap[0]:
                heapq.heappop(myheap)
                heapq.heappush(myheap,i)

        return myheap[0]



        