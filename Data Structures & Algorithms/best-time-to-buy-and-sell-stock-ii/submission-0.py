class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -float('inf') 
        free = 0
        for price in prices:
            prev_hold = hold
            hold = max(hold, free - price)
            free = max(free, prev_hold + price)
        return free

        