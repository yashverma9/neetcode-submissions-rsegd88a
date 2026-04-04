from collections import defaultdict
import heapq
class Twitter:
    # Optimal, time - O(F + 10logF), space- O(F)... F is no. of followee
    '''
    We use same logic as how we can solve 'merge k sorted lists' using a heap. We take
    the last tweet from each followee and put its -count(ts) into maxheap along with tweetId,
    followeeId, the next index to add (index-1). So now we have a heap of size F with each
    one recent tweet of each followee. Now, we pop the latest (lowest negative count) tweet,
    add that to res. We push the next recent tweet of that user,
    and continue so on till res is size 10 or heap is over.
    '''

    def __init__(self):
        self.following = defaultdict(set) # {userId: set[followingIds]}
        self.tweets = defaultdict(list) # {userId: [tweetIds]}
        self.count = 0 # Use decrementing count for time, decrement because maxHeap needs negative values in python

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        maxHeap = []
        res = []
        self.following[userId].add(userId) # Adding self as follower (mentioned in Q)

        for followee in self.following[userId]:
            if self.tweets[followee]:
                index = len(self.tweets[followee]) - 1
                (count, tweetId) = self.tweets[followee][index]
                maxHeap.append((count, tweetId, followee, index-1))
        
        # O(F)
        heapq.heapify(maxHeap)
            
        # O(10logF) - 10 pops and 10 pushes max into F tweets - 1 for each followers (F)
        while maxHeap and len(res) < 10:
            (count, tweetId, followee, index) = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                (count, tweetId) = self.tweets[followee][index]
                heapq.heappush(maxHeap, (count, tweetId, followee, index-1))
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
                
