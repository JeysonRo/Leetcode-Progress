class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = -1
        for i in range(2, len(colors)):
            if colors[i] == 'A' and colors[i-1] == 'A' and colors[i-2] == 'A':
                count += 1
            elif colors[i] == 'B' and colors[i-1] == 'B' and colors[i-2] == 'B':
                count -= 1
        
        if count >= 0:
            return True
        else:
            return False