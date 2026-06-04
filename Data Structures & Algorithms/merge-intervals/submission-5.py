class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        sorted_ints = sorted(intervals, key=lambda i: i[0])
        res = [sorted_ints[0]]
       
        for i, j in sorted_ints:
            end = res[-1][1]
            if i <= end:
                res[-1][1] = max(end, j)
            else:
                res.append([i,j])
        return res



        