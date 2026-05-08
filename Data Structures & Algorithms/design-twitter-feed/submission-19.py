class Twitter:

    def __init__(self):
        self.tweetMap = {}
        self.followMap = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId in self.tweetMap:
            self.tweetMap[userId].append((-self.time, tweetId))
        else:
            self.tweetMap[userId] = [(-self.time,tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        for person in self.followMap[userId]:
            if person in self.tweetMap:
                tweets = self.tweetMap[person]
                index = len(tweets) - 1
                count,tid = tweets[index]
                heapq.heappush(h,(count,tid,index,person))
        
        res= []
        while h and len(res) < 10:
            count,tid,index,person = heapq.heappop(h)
            res.append(tid)
            index -= 1
            tweets = self.tweetMap[person]
            if index >-1:
                count,tid = tweets[index]
                heapq.heappush(h,(count,tid,index,person))
        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].add(followeeId)
        else:
            self.followMap[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId  in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
