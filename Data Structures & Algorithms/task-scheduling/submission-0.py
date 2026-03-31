class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        inputs = Counter(tasks)
        myheap = [-x for x in inputs.values()]

        heapq.heapify(myheap)

        queue = deque()
        time = 0

        while queue or myheap:
            time+=1
            if myheap:
                cnt = 1 + heapq.heappop(myheap)

                if cnt:
                    queue.append([cnt, time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(myheap,queue.popleft()[0])

        return time
        