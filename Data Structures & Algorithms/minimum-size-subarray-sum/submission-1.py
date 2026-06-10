class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        current_sum = 0
        left = 0
        current_len = 0
        best_len = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target and left < len(nums):
                current_lent = right - left + 1
                current_sum -= nums[left]
                best_len = min(best_len, current_lent)
                left += 1
        return best_len if best_len != float('inf') else 0