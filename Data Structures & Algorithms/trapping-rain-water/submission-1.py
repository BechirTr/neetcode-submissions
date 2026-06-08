class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft , maxRight = height[left], height[right]
        water = 0

        while left < right:
            if maxLeft < maxRight:
                water += maxLeft - height[left]
                left += 1
                maxLeft = max(maxLeft, height[left])
            else:
                water += maxRight - height[right]
                right -= 1
                maxRight = max(maxRight, height[right])
        return water
