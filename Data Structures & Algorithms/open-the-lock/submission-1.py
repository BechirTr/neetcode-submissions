from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        dist = {"0000": 0}
        q = deque(["0000"])

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node == target:
                    return dist[node]
                neighbors = []
                for i in range(4):
                    e = int(node[i])
                    
                    forward = list(node)
                    forward[i] = str(e + 1) if e < 9 else "0"
                    neighbors.append(''.join(forward))
                    
                    backward = list(node)
                    backward[i] = str(e - 1) if e > 0 else "9"
                    neighbors.append(''.join(backward))
                for nei in neighbors:
                    if nei in dist or nei in deadends:
                        continue
                    dist[nei] = dist[node] + 1
                    q.append(nei)
        return dist[target] if target in dist else -1