class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if ((i == 0) or (i == len(board) - 1) or ((j == 0) or (j == len(board[0]) - 1))):
                    continue
                if (board[i][j] == 'X' or board[i][j] == 'V'):
                    continue
                if (self.dfs(board, i, j)):
                    self.flip(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 'V'):
                    board[i][j] = 'O'

    def dfs(self, board, i, j) -> bool:
        if(i<0 or i>=len(board) or j<0 or j>=len(board[0])):
            return False
        if (board[i][j] == 'O'):
            board[i][j] = 'V'
            return (self.dfs(board, i - 1, j) and self.dfs(board, i + 1, j) and self.dfs(board, i, j - 1) and self.dfs(board, i, j + 1))
        elif (board[i][j] == 'X' or board[i][j] == 'V'):
            return True
        else:
            return False

    def flip(self, board, i, j):
        if(i<0 or i>=len(board) or j<0 or j>=len(board[0])):
            return
        if (board[i][j] == 'X'):
            return
        board[i][j] = 'X'

        self.flip(board, i - 1, j)
        self.flip(board, i + 1, j)
        self.flip(board, i, j - 1)
        self.flip(board, i, j + 1)