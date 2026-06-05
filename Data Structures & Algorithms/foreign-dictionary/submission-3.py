from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adict = defaultdict()
        #build keys 
        for k in ''.join(words):
            adict[k] = []
       
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            l = min(len(w1),len(w2))
            for j in range(l):
                if w1[j] != w2[j]:
                    adict[w1[j]].append(w2[j])
                    break
            else:
                if len(w1) > len(w2):
                    return ""
  
        visited = defaultdict(int)  # 0 = unvisited, 1 = visiting, 2 = done
        res = []

        def dfs(node):
            if visited[node] == 1:
                return False 
            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in adict[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2
            res.append(node)
            return True

        for node in adict:
            if not dfs(node):
                return "" 

        return(''.join(res)[::-1])

        