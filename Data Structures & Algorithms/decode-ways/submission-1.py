
import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        """@functools.lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            res = dfs( i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i]=='2' and s[i+1] < '7')):
                    res += dfs(i + 2)
            return res
        return dfs(0)"""
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i+1] 
                if i < len(s) - 1 and (s[i] == '1' or (s[i]=='2' and s[i+1] < '7')):
                    dp[i] += dp[i+2]
                
        return dp[0]
                
        



            
