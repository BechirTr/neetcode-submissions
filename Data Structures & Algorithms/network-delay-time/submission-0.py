import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def build_graph(times):
            graph = defaultdict()
            #build keys
            for i in range(1, n+1):
                graph[i] = []
            # add (neighbor , weight)
            for time in times:
                key, nei, wei = time
                graph[key].append((nei, wei))
            return graph
        
        
        def dijikstra(graph, start):

            dist = defaultdict(lambda: float("inf"))
            dist[start] = 0

            heap = [(0, start)] 

            while heap:
                cur_dist, node = heapq.heappop(heap)
                
                if cur_dist > dist[node]:
                    continue
                for nei, time in graph[node]:
                    new_dist = cur_dist + time
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))

            if len(dist) != len(graph):
                return -1
            
            return max(dist.values())

        graph = build_graph(times)
        return dijikstra(graph, k)