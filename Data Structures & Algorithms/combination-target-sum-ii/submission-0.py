class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])   # snapshot and record
                return
            
            for i in range(start, len(candidates)):
               
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if remaining - candidates[i] < 0:
                    break 
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, path)
        return result