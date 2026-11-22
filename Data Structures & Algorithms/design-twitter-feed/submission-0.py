class Twitter:

    def __init__(self):
        self.time = 0
        self.following_map = defaultdict(set)
        self.posts_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.posts_map[userId].append([self.time, userId, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        following = list(self.following_map[userId])[:]
        following.append(userId)
        raw_feed = []
        for f in following:
            raw_feed.extend(self.posts_map[f])
        heapq.heapify(raw_feed)
        feed = []
        count = 10
        while count > 0 and raw_feed:
            post = heapq.heappop(raw_feed)
            feed.append(post[2])
            count -= 1
        
        return feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.following_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        target_set = self.following_map[followerId]
        if followeeId in target_set:
            target_set.remove(followeeId)
        
