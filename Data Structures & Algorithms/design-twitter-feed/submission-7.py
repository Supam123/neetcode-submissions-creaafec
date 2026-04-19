class Twitter:

    def __init__(self):
        self.tweetMap = {} # user id to tweets
        self.followerMap = {} # userid to followeee ids
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(-self.count,tweetId)]
        else:
            self.tweetMap[userId].append((-self.count,tweetId))
            

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        if userId not in self.followerMap:
            self.followerMap[userId] = set()
        self.followerMap[userId].add(userId)

        for person in self.followerMap[userId]:
            if person in self.tweetMap:
                tweets = self.tweetMap[person]
                index = len(tweets) - 1
                count,tweetId = tweets[index]
                heapq.heappush(h,(count,tweetId,person,index))
        res = []
        while h and len(res) < 10:
            count,tweetId,person,index = heapq.heappop(h)
            res.append(tweetId)
            tweets = self.tweetMap[person]
            index -= 1
            count,tweetId = tweets[index]
            if index >= 0 :
                heapq.heappush(h,(count,tweetId,person,index))
        return res






        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerMap:
            self.followerMap[followerId] = set([followeeId])
        else:
            self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId  in self.followerMap:
            self.followerMap[followerId].discard(followeeId)

        

        
