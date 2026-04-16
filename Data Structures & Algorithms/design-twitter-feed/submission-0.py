class Twitter:

    def __init__(self):
        self.tweetMap = {} #userId-> tweetId
        self.followMap = {} #followerId -> followeeID
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if  userId not in self.tweetMap: 
            self.tweetMap[userId] = [(-self.count,tweetId)]
        else:
            self.tweetMap[userId].append((-self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        if userId not in self.followMap:
            self.followMap[userId] = set() # user id never followed anyone so they need to see there tweeets only
        self.followMap[userId].add(userId)
        
        for person in self.followMap[userId]:
            if person in self.tweetMap:
                tweet = self.tweetMap[person]
                index = len(tweet) - 1
                count,tweetId = tweet[index]
                heapq.heappush(heap,(count,tweetId,person,index))
        
        res = []
        while heap and len(res) < 10:
            count,tweetId,person,index = heapq.heappop(heap)
            res.append(tweetId)
            index = index - 1
            if index >= 0:
                tweet = self.tweetMap[person]
                count,tweetId = tweet[index]
                heapq.heappush(heap,(count,tweetId,person,index))
        return res

     



      

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        else:
            self.followMap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap: #look in the hashmap in constant time 
            self.followMap[followerId].discard(followeeId) # remove from the set in constant time 
        
