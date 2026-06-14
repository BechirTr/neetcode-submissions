class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [1 if matrix[0][j] == '1' else 0 for j in range(n)]
        max_side = max(dp)                           # ← track as we go

        for i in range(1, m):
            prev = dp[0]
            dp[0] = int(matrix[i][0] == '1')
            max_side = max(max_side, dp[0])          # ← update

            for j in range(1, n):
                temp = dp[j]
                if matrix[i][j] == '1':
                    dp[j] = 1 + min(dp[j], dp[j-1], prev)
                else:
                    dp[j] = 0
                max_side = max(max_side, dp[j])      # ← update
                prev = temp

        return max_side ** 2