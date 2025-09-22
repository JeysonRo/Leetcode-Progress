class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board[0])
        n = len(board)
        if m*n == 1 and len(word) == 1:
            if board[0][0] == word[0]:
                return True

        def dfs(snake, cur, index):
            col = cur[0]
            row = cur[1]
            if index == len(word):
                return True
            elif word[index] != board[row][col]:
                return False
            elif (col, row) in snake:
                return False
            
            snake.add(cur)
            # traverse right
            if cur[0] < m - 1:
                right = dfs(snake, (col + 1, row), index + 1)
            else:
                right = False
            # traverse left
            if cur[0] > 0:
                left = dfs(snake, (col -1 , row), index + 1)
            else:
                left = False
            # traverse up
            if cur[1] > 0:
                up = dfs(snake, (col, row - 1), index + 1)
            else:
                up = False
            # traverse down
            if cur[1] < n - 1:
                down = dfs(snake, (col, row + 1), index + 1)
            else:
                down = False
            snake.remove(cur)
            
            return up or down or left or right

        i = 0
        while i < m*n:
            cur = (i % m, i // m)
            if board[cur[1]][cur[0]] == word[0]:
                res = dfs(set(), cur, 0)
                if res:
                    return True
                
            i += 1
        
        return False