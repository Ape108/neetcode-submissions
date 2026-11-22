class Twitter:

    def __init__(self):
        self.time = 0
        self.following_map = defaultdict(set)
        self.posts_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        minHeap = []
        self.following_map[userId].add(userId)
        for f in self.following_map[userId]:
            if f in self.posts_map:
                    index = len(self.posts_map[f]) - 1
                    time, tweetId = self.posts_map[f][index]
                    minHeap.append([time, tweetId, f, index-1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, f, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.posts_map[f][index]
                heapq.heappush(minHeap, [time, tweetId, f, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
        
