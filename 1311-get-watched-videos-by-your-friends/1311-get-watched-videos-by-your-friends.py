class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        n = len(friends)
        
        count = defaultdict(lambda :0)
        q = deque([id])
        depth = 0
        visited = set([id])
        while q:
            for i in range(len(q)):
                person = q.popleft()
                if depth == level:
                    for video in watchedVideos[person]:
                        count[video] += 1
                    continue
                
                for friend in friends[person]:
                    if friend not in visited:
                        q.append(friend)
                        visited.add(friend)
            depth += 1

        return sorted(count, key=lambda x: (count[x], x))