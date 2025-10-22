class Twitter:

    def __init__(self):
        self.users = {} # users[userID] = [following set(), posts]
        # posts[i] = tweetID
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [set(),[]]
        self.users[userId][1].append((self.time, tweetId))
        # print("user: ", userId, " posted: ", tweetId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            # print("Error: getNewsFeed: user does not exist")
            return []
        # get list of posts
        heap = self.users[userId][1].copy()
        for followId in self.users[userId][0]:
            heap.extend(self.users[followId][1])
        
        heapq._heapify_max(heap)
        res = []
        while heap and len(res) < 10:
            tweet = heapq._heappop_max(heap)
            res.append(tweet[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [set(),[]]
        if followeeId not in self.users:
            self.users[followeeId] = [set(),[]]
        self.users[followerId][0].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            print("Error: user cannot follow self")
            return
        if followerId not in self.users:
            self.users[followerId] = [set(),[]]
        if followeeId not in self.users:
            self.users[followeeId] = [set(),[]]
        if followeeId in self.users[followerId][0]:
            self.users[followerId][0].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)