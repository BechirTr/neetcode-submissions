class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            return s == s[::-1]
        result = []
        current = []
        def backtrack(start):
            if start >= len(s):
                result.append(current[:])
                return 
            
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    current.append(s[start:end+1])
                    backtrack(end+1)
                    current.pop()
        backtrack(0)
        return result

            