class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myheap = nums
        heapq.heapify(self.myheap)
        print(self.myheap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.myheap, val)
        return heapq.nlargest(self.k,self.myheap)[-1]
        
