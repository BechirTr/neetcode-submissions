class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        used = [False]*len(nums)
        result = []
        def backtrack(current, used):
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    backtrack(current, used)
                    current.pop()
                    used[i] = False
        backtrack(current, used)
        return result