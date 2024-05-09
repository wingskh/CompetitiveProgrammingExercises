# https://leetcode.com/problems/task-scheduler/
from heapq import heapify, heappop
from typing import List
from collections import defaultdict

# Method: Heap
class Twitter:
    def __init__(self):
        self.tweetList = defaultdict(list)
        self.followingList = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetList[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followingList[userId].add(userId)
        tweetListHeap = []
        for user in self.followingList[userId]:
            tweetListHeap.extend(self.tweetList[user])

        heapify(tweetListHeap)
        return [heappop(tweetListHeap)[1] for _ in range(min(len(tweetListHeap), 10)) if tweetListHeap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].discard(followeeId)

# Method: Hash Table
class Twitter:
    def __init__(self):
        self.postList = []
        self.followingList = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postList.append((userId, tweetId))
        if userId not in self.followingList:
            self.followingList[userId] = set([userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tenRecentFeeds = []
        for user, feedId in reversed(self.postList):
            if user in self.followingList[userId]:
                tenRecentFeeds.append(feedId)
                if len(tenRecentFeeds) == 10:
                    break
        return tenRecentFeeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followingList:
            self.followingList[followerId] = set([followerId])

        if followeeId not in self.followingList:
            self.followingList[followeeId] = set([followeeId])

        self.followingList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].discard(followeeId)


action = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
actionParams = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# output = [null,null,[5],null,null,[5],null,[5]]
action = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
actionParams = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
# output = [null,null,[5],null,null,[6,5],null,[5]]
action = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
actionParams = [[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]]
# output = [null,null,null,null,null,null,null,null,null,null,null,null,[11,22,333,505,94,2,10,13,101,3]]

obj = Twitter()
result = [[]]
for i in range(1, len(action)):
    if action[i] == "postTweet":
        obj.postTweet(actionParams[i][0], actionParams[i][1])
        result.append([])
    elif action[i] == "getNewsFeed":
        tweets = obj.getNewsFeed(actionParams[i][0])
        result.append(tweets)
    elif action[i] == "follow":
        obj.follow(actionParams[i][0], actionParams[i][1])
        result.append([])
    elif action[i] == "unfollow":
        obj.unfollow(actionParams[i][0], actionParams[i][1])
        result.append([])

print(result)
