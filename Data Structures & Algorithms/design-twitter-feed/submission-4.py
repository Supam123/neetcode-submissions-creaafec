class Twitter:

    def __init__(self):
        self.tweetMap = {} # userid -> tweetid
        self.followMap = {} # userid -> followeeid
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(self.count,tweetId)]
        else:
            self.tweetMap[userId].append((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # return only atmost 10 tweets of users followers and user including self.
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        #we will go to each follower in the follow map and pick up 
        #the most reccent tweet from last adn that we will add to our heap
        h = []
        for person in self.followMap[userId]:
            if person in self.tweetMap:
              tweets  = self.tweetMap[person] #get all the tweets for that person
              index = len(tweets) - 1
              count = -1*tweets[index][0]
              tweetId = tweets[index][1]
              heapq.heappush(h,(count,tweetId,index,person))
        i = 0
        res = []
        while h and i < 10:
            count,tweetId,index,person= heapq.heappop(h)
            res.append(tweetId)
            if index - 1 >= 0:
                index -= 1
                tweets = self.tweetMap[person]
                count = -1*tweets[index][0]
                tweetId = tweets[index][1]
                heapq.heappush(h,(count,tweetId,index,person))
            i += 1
        return res







    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        else:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
    
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)