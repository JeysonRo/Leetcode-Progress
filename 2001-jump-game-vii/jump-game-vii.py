class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # s = binary string | s[0] == '0'
        # can only jump to '0's
        # can only jump between i + minJump and i + maxJump
        if s[-1] == '1':
            return False

        spaces_q = deque() # index of possible spaces
        spaces_set = set() # index of possible spaces
        spaces_q.appendleft(0)
        farthest = 0
        while spaces_q:
            index = spaces_q.pop()
            for j in range(max(index + minJump, farthest), min(index + maxJump + 1, len(s))):
                if j == len(s) - 1:
                    return True
                if s[j] == '0' and j not in spaces_set:
                    spaces_set.add(j)
                    spaces_q.appendleft(j)
                
            farthest = index + maxJump
                
        return False