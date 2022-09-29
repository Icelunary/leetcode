class Node:
    def __init__(self, i):
        self.val = i
        self.adj = []
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        k = len(connections)
        if n-1 > k:
            return -1
        myG = {}
        visitedNode = set()
        visitedEdge = set()
        for i in range(n):
            myG[i] = []
        for a, b in connections:
            myG[a].append(b)
            myG[b].append(a)
        groups = 0
        extra = 0
        # print(myG)
        for node in range(n):
            if node not in visitedNode:
                groups += 1
                extra += self.bfs(node, myG, visitedEdge, visitedNode)
                print(extra)
        # print(myG)
        return groups - 1
        
    def bfs(self, root: int, graph: map, visitedEdge: set, visitedNode: set) -> int:
        q = deque([root])
        extra = 0
        visitedNode.add(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for adj in graph[node]:
                    if adj in visitedNode:
                        if (node, adj) not in visitedEdge and (adj, node) not in visitedEdge:
                            extra += 1
                    else:
                        q.append(adj)
                        visitedNode.add(adj)
                        visitedEdge.add((node, adj))
        return extra