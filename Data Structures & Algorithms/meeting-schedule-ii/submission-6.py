"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda i: i.start)
        heap = []
        for meeting in intervals:
            if heap and heap[0] <= meeting.start:
                heapq.heappop(heap)
                heapq.heappush(heap, meeting.end)
            else:
                heapq.heappush(heap, meeting.end)
        return len(heap)