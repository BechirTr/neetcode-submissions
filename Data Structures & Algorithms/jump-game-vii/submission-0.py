from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        
        def get_neighbors(i):
            neighbors = []
            for j in range(i, len(s)):
                if i + minJump <= j and j <= i + maxJump and s[j]=='0':
                    neighbors.append(j)
            return neighbors
        
        def bfs(start, target):
            visited = set([start])
            queue = deque([start])

            while queue:
                node = queue.popleft()
                if node == target:
                    return True 
                for neighbor in get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return False
        return bfs(0,len(s)-1)
        