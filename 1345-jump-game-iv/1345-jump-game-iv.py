class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        
        adjacency_list = {}
        n = len(arr)
        for i in range(n):
            if arr[i] not in adjacency_list:
                adjacency_list[arr[i]] = [i]
            else:
                adjacency_list[arr[i]].append(i)
        
        def bfs(adjacency_list, arr):
            visit = [0 for i in range(len(arr))]
            n = len(arr)
            dis = 0
            q = deque([0])
            cnt = 0
            while q:
                for i in range(len(q)):
                    # print(dis, q)
                    index = q.popleft()
                    node = arr[index]
                    value = node
                    visit[index] = 1
                    if index == n - 1:
                        print(cnt)
                        return dis
                    for adjacency_node in adjacency_list[value]:
                        if visit[adjacency_node] == 0:
                            q.append(adjacency_node)
                            visit[index] == 1
                        cnt += 1
                    if index > 0 and visit[index-1] == 0:
                        q.append(index-1)
                        visit[index-1] = 1
                        cnt += 1
                    if index < n-1 and visit[index+1] == 0:
                        q.append(index+1)
                        visit[index+1] = 1
                        cnt += 1
                    adjacency_list[value] = []
                
                dis += 1       
        res = bfs(adjacency_list, arr)
        return res