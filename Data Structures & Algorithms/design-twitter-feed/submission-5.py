from collections import defaultdict
import heapq
import time
class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # hashmap userId: [userIds]
        self.tweets = defaultdict(list) # hashmap userId: [tweetIds]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((time.time(),tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for user in self.following[userId]:
            if user != userId:
                for tweet in self.tweets[user]:
                    heapq.heappush(minHeap, tweet)
                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)
        
        for tweet in self.tweets[userId]:
            heapq.heappush(minHeap, tweet)
            if len(minHeap) > 10:
                heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap))
        res.sort(reverse = True)
        return [tweet[1] for tweet in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
