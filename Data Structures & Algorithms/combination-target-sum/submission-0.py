class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])   # snapshot and record
                return
            if remaining < 0:        # ← prune dead branches
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)
                path.pop()
        backtrack(0, target, path)
        return result