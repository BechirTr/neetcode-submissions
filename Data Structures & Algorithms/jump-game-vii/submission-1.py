from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        dp = [False]*len(s)
        dp[0] = True
        counter = 0
        for i in range(1,len(s)):
            
            if  minJump <= i and dp[i - minJump]:
                counter += 1
            if maxJump < i and dp[i - maxJump - 1]:
                counter -= 1
        
            if counter > 0 and s[i]=='0':
                dp[i] = True
            
        return dp[-1]
    
    


        