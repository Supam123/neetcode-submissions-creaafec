class Twitter:

    def __init__(self):
        self.tweetMap = {} # userid = tweetid
        self.followMap = {} # followerid =  followeeid
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(-self.count,tweetId)]
        else:
            self.tweetMap[userId].append((-self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        h = []
        for person in self.followMap[userId]:
            if person in self.tweetMap:
                tweets =  self.tweetMap[person]
                index = len(tweets) - 1
                count,t_id =  tweets[index]
                heapq.heappush(h, (count,t_id,index,person))
        res = []
        while h and len(res) < 10:
            count,t_id,index,person  =  heapq.heappop(h)
            res.append(t_id)
            index -= 1
            if index > -1 :
                tweets = self.tweetMap[person]
                count,t_id =  tweets[index]
                heapq.heappush(h, (count,t_id,index,person))
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        