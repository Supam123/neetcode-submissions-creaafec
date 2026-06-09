class Twitter:

    def __init__(self):
        self.tweetMap = {}
        self.followerMap = {}
        self.count = 1
      
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId in self.tweetMap:
            self.tweetMap[userId].append((-self.count,tweetId))
        else:
            self.tweetMap[userId] = [(-self.count,tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followerMap:
            self.followerMap[userId] = set()
        self.followerMap[userId].add(userId)
        h = []
        for person in self.followerMap[userId]:
            if person in self.tweetMap:
                tweets = self.tweetMap[person]
                index = len(tweets)-1
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
        if followerId not in self.followerMap:
            self.followerMap[followerId] = set()
        self.followerMap[followerId].add(followeeId)
        
 


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerMap:
            self.followerMap[followerId].discard(followeeId)
    
        




        
