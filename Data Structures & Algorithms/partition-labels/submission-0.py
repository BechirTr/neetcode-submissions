from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastidx = defaultdict()
        for i,e in enumerate(s):
            lastidx[e] = i 
        size = 0
        res = []
        end = 0
        for i in range(len(s)):
            size+=1
            end = max(end, lastidx[s[i]])
            if i==end:
                res.append(size)
                size = 0 
        return res

