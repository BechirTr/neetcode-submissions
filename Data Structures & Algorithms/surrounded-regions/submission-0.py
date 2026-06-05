class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def find_O(board):
            res = []
            for r in range(1, rows-1):
                if board[r][0] == 'O':
                    res.append((r,0))
                if board[r][cols-1] == 'O':
                    res.append((r,cols-1))
            for c in range(cols):
                if board[0][c] == 'O':
                    res.append((0, c))
                if board[rows - 1][c] == 'O':
                    res.append((rows - 1, c))
            return res
        nodes = find_O(board)
        for r,c in nodes:
            board[r][c] = "#"
            stack = [(r,c)]
            while stack:
                cr, cc = stack.pop()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and 
                        board[nr][nc] == "O"):
                        board[nr][nc] = "#"
                        stack.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"