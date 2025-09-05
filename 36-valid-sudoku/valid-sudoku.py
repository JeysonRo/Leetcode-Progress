class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bank = set()
        # check by row
        for i in range(len(board)):
            bank = set()
            for j in range(len(board)):
                if not board[i][j].isdigit():
                    continue
                elif board[i][j] in bank:
                    print("row: " + str(i) + " col: " + str(j) + " found duplicate: " + str(board[i][j]))
                    return False
                else:
                    bank.add(board[i][j])
        
        # check by col
        bank = set()
        for i in range(len(board)):
            bank = set()
            for j in range(len(board)):
                if not board[j][i].isdigit():
                    continue
                elif board[j][i] in bank:
                    print("row: " + str(i) + " col: " + str(j) + " found duplicate: " + str(board[j][i]))
                    return False
                else:
                    bank.add(board[j][i])

        # check by sub-box
        bank = set()
        for subrow in range(3):
            for subcol in range(3):
                bank = set()
                for i in range(3):
                    for j in range(3):
                        if not board[i + 3*subrow][j + 3*subcol].isdigit():
                            continue
                        elif board[i + 3*subrow][j + 3*subcol] in bank:
                            return False
                        else:
                            bank.add(board[i + 3*subrow][j + 3*subcol])


        return True