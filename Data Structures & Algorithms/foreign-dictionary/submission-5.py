from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indeg = defaultdict(int)
        adict = defaultdict(list)
        #build keys 
        for k in ''.join(words):
            adict[k] = []
            indeg[k] = 0
       
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            l = min(len(w1),len(w2))
            for j in range(l):
                if w1[j] != w2[j]:
                    indeg[w2[j]] += 1
                    adict[w1[j]].append(w2[j])
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        q = deque([node for node in adict if indeg[node] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adict[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if len(order) != len(adict):
            return ""  # cycle

        return "".join(order)




        