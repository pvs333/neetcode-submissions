import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1,n+1):
            graph[i] = []
        for u,v,t in times:
            graph[u].append((v,t))
        dists = {}
        for node in graph:
            dists[node] = float('inf')
        dists[k] = 0
        pq = [(0, k)]

        while pq:
            cdist, cnode = heapq.heappop(pq)
            for node, weight in graph[cnode]:
                dist = cdist + weight
                if dist < dists[node]:
                    dists[node] = dist
                    heapq.heappush(pq, (dist, node))
        
        dits = []
        for i in dists:
            if dists[i] == float('inf'):
                return -1
            dits.append(dists[i])
        return max(dits)

        