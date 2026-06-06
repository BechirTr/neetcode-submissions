class Solution:
    def numSquares(self, n: int) -> int:
        candidates = [ i**2 for i in range(1,n+1) if i**2 <= n]
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 
        for num in candidates:
            for j in range(num, n + 1):  # FORWARD
                dp[j] = min(dp[j], dp[j - num] + 1)  # or dp[j] += dp[j - num] for count

        return dp[n]