class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        

        def bellman_ford(n,k, edges, start, end):
            

            dist = [float('inf')]*n
            dist[start] = 0

            for _ in range(k+1):
                next_dist = dist[:]
                for u,v,w in edges:
                    if dist[u] != float('inf') and dist[u] + w < next_dist[v]:
                        next_dist[v] = dist[u] + w
                       
                dist = next_dist
            if dist[end] == float('inf'):
                return -1
            else:
                return dist[end]
        
        return bellman_ford(n, k, flights, src, dst)
