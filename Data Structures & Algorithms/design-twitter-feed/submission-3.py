import heapq


class Twitter:
    def __init__(self):
        self.user_followings: dict[int, set] = {}
        self.user_posts: dict[int, list[tuple[int, int]]] = {}
        self.tweet_counter: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts:
            self.user_posts[userId] = [(-self.tweet_counter, tweetId)]
        else:
            self.user_posts[userId].append((-self.tweet_counter, tweetId))
        self.tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_followings:
            return [el[1] for el in self.user_posts[userId][:-11:-1]]
        
        if userId in self.user_posts:
            heap = [(*self.user_posts[userId][-1], len(self.user_posts[userId]) - 2, userId)] 
        else:
            heap = []

        for user in self.user_followings[userId]:
            heapq.heappush(heap, (*self.user_posts[user][-1], len(self.user_posts[user]) - 2, user))

        result = []
        while len(result) < 10 and heap:
            _, tweetId, nextTweetId, currUserId = heapq.heappop(heap)
            result.append(tweetId)
            if nextTweetId != -1:
                heapq.heappush(heap, (*self.user_posts[currUserId][nextTweetId], nextTweetId - 1, currUserId))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followings:
            self.user_followings[followerId] = {followeeId}
        else:
            self.user_followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followings:
            if followeeId in self.user_followings[followerId]:
                self.user_followings[followerId].remove(followeeId)
