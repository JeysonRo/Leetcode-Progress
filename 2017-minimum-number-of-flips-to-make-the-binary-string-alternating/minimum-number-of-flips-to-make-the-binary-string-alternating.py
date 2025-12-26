class Solution:
    def minFlips(self, s: str) -> int:
        original_len = len(s)
        s += s
        goal = ['','']
        a = 0
        b = 1
        for i in range(len(s)):
            goal[a] += '0'
            goal[b] += '1'
            a, b = b, a
        goal0 = 0
        goal1 = 0
        maxmatch = 0
        i = 0
        while i < len(s):
            if s[i] == goal[0][i]:
                goal0 += 1
            else:
                goal1 += 1
            if i >= original_len:
                if s[i] == goal[0][i-original_len]:
                    goal0 -= 1
                else:
                    goal1 -= 1
            # print("goal0: ", goal0, "\ngoal1: ", goal1)
            maxmatch = max(maxmatch, goal0, goal1)
            i += 1

        # print(maxmatch)
        return original_len - maxmatch