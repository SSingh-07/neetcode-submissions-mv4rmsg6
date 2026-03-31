class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        myheap =[-x for x in stones]
        heapq.heapify(myheap)

        while len(myheap) > 1:
            a = heapq.heappop(myheap)
            b = heapq.heappop(myheap)

            if abs(a-b):
                heapq.heappush(myheap,-1*abs(a-b))

            # print(myheap)
        return -myheap[0] if len(myheap) else 0
        