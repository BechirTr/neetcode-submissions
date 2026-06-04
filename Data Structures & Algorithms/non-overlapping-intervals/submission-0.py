class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda i: i[1])
        keep = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = keep[-1][1]
            if lastend > start:
                continue
            else:
                keep.append([start, end])

        return len(intervals) - len(keep)

