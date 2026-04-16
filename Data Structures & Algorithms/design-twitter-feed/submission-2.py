import heapq

class Twitter:

    def __init__(self):
        # O(1) time | O(1) space — creating empty dicts and counter
        self.tweetMap = {}    # userId -> list of (-count, tweetId)
        self.followMap = {}   # followerId -> set of followeeIds
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1) time | O(1) space — list append is O(1) amortized
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(-self.count, tweetId)]
        else:
            self.tweetMap[userId].append((-self.count, tweetId))

    def getNewsFeed(self, userId: int) -> list:
        # O(f log f) time | O(f) space
        # f = number of people we check (user + followers)
        # Building heap: loop f people, each heappush is O(log f) -> O(f log f)
        # Popping: up to 10 pops, each O(log f) -> O(10 log f) -> O(log f)
        # Total: O(f log f)
        # Space: heap holds at most f entries -> O(f)

        heap = []

        # if user never followed anyone, create empty set
        # so we can still add themselves and see their own tweets
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)

        # grab only the MOST RECENT tweet from each person (last in list)
        # this is the merge k sorted lists trick — don't load all tweets
        for person in self.followMap[userId]:
            if person in self.tweetMap:
                tweets = self.tweetMap[person]
                index = len(tweets) - 1
                count, tweetId = tweets[index]
                heapq.heappush(heap, (count, tweetId, person, index))

        res = []
        while heap and len(res) < 10:
            count, tweetId, person, index = heapq.heappop(heap)
            res.append(tweetId)
            # go back one tweet for whoever we just popped
            # index walks backwards through their tweet list
            # we use index instead of .pop() so we don't delete their tweets
            index = index - 1
            if index >= 0:
                count, tweetId = self.tweetMap[person][index]
                heapq.heappush(heap, (count, tweetId, person, index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # O(1) time | O(1) space — set add is O(1)
        if followerId not in self.followMap:
            self.followMap[followerId] = {followeeId}
        else:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(1) time | O(1) space — set discard is O(1)
        # discard instead of remove so it doesn't crash if not found
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)



            