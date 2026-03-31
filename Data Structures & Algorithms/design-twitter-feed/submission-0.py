class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                maxHeap.append([count, tweetId, followee, index - 1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetid, followee, index = heapq.heappop(maxHeap)
            res.append(tweetid)
            if index >= 0:
                count, tweetid = self.tweetMap[followee][index]
                heapq.heappush(maxHeap,[count, tweetid, followee, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
