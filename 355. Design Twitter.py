from collections import defaultdict, deque

class Twitter(object):

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId):
        newsPool = []
        for u in self.followees[userId] | {userId}:
            newsPool.extend(self.tweets[u][-10:])      ## take the top 10 tweets from each user u
        heapq.heapify(newsPool)

        res = []
        for i in range(10):
            if not newsPool:
                break
            item = heapq.heappop(newsPool)
            res.append(item[1])
        return res

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)



if __name__ == '__main__':
    t = Twitter()
    t.postTweet(1, 5)
    t.postTweet(1, 4)
    t.postTweet(2, 3)
    t.follow(1, 2)
    print(t.getNewsFeed(1))
    t.unfollow(1, 2)
    print(t.followees)