class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # run bfs from every 'O' on the edge to find safe cells
        # convert all other cells to 'X'
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        queue = deque()

        for col in range(COLS):
            if board[0][col] == 'O':
                visited.add((0, col))
                queue.appendleft((0, col))
            if board[ROWS-1][col] == 'O':
                visited.add((ROWS-1, col))
                queue.appendleft((ROWS-1, col))
        for row in range(ROWS):
            if board[row][0] == 'O':
                visited.add((row, 0))
                queue.appendleft((row, 0))
            if board[row][COLS-1] == 'O':
                visited.add((row, COLS-1))
                queue.appendleft((row, COLS-1))

        print(visited)
        while queue:
            x,y = queue.pop()
            if x < ROWS - 1 and (x + 1, y) not in visited and board[x+1][y] == 'O':
                queue.appendleft((x+1,y))
                visited.add((x+1,y))
            if x > 0 and (x - 1, y) not in visited and board[x-1][y] == 'O':
                queue.appendleft((x-1,y))
                visited.add((x-1,y))
            if y < COLS - 1 and (x, y + 1) not in visited and board[x][y+1] == 'O':
                queue.appendleft((x,y+1))
                visited.add((x,y+1))
            if y > 0 and (x, y - 1) not in visited and board[x][y-1] == 'O':
                queue.appendleft((x,y-1))
                visited.add((x,y-1))

        print(visited)
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited:
                    board[i][j] = 'X'