class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        l , r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            if heights[l] < heights[r]:
                water = heights[l]*(r - l)
                max_water = max(max_water, water)
                l += 1
            else:
                water = heights[r]*(r - l)
                max_water = max(max_water, water)
                r -= 1
        return max_water
        