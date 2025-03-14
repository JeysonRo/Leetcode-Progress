class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # grid[column][row]
        colsize = len(grid)
        rowsize = len(grid[0])
        answer = []
        rowpos = 0
        colpos = 0

        print("colsize", colsize)
        print("rowsize",  rowsize)

        for ball in range(rowsize): # range of n
            rowpos = ball
            colpos = 0
            while(colpos < colsize + 1): # range of m
                if colpos >= colsize:
                    # ball fell out of bottom
                    answer.append(rowpos)
                    break
                if grid[colpos][rowpos] == 1:
                    # go right
                    if rowpos + 1 >= rowsize:
                        # stuck on right edge
                        answer.append(-1)
                        break
                    elif grid[colpos][rowpos + 1] == -1:
                        # stuck on V
                        answer.append(-1)
                        break
                    else:
                        # move down and right
                        rowpos += 1
                        colpos += 1
                        continue
                else:
                    # go left
                    if rowpos - 1 < 0:
                        # stuck on left wall
                        answer.append(-1)
                        break
                    elif grid[colpos][rowpos - 1] == 1:
                        # stuck on V
                        answer.append(-1)
                        break
                    else:
                        # move down and left
                        rowpos -= 1
                        colpos += 1
                        continue

        return answer
