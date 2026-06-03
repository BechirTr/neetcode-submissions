class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if board[i][j] == '#' or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            found = backtrack(i-1,j,k+1) or backtrack(i+1,j,k+1) or backtrack(i,j-1,k+1) or backtrack(i,j+1,k+1)
            board[i][j] = temp
            return found 
        for i in range(n):
                for j in range(m):
                    if backtrack(i, j, 0):   # start matching from word[0]
                        return True
        return False
