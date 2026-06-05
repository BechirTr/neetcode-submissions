"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
from itertools import chain
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        heap = []  # stores end times of active meetings
        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heapreplace(heap, i.end)  # reuse room
            else:
                heapq.heappush(heap, i.end)     # new room needed
        return len(heap)