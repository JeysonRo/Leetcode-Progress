class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # O(1) space
        sp = len(s) - 1
        tp = len(t) - 1

        s_skip = 0
        t_skip = 0

        while sp >= 0 or tp >= 0:
            if sp >= 0 and s[sp] == '#':
                sp -= 1
                s_skip += 1
                continue
            if tp >= 0 and t[tp] == '#':
                tp -= 1
                t_skip += 1
                continue
            if s_skip > 0:
                sp -= 1
                s_skip -= 1
                continue
            if t_skip > 0:
                tp -= 1
                t_skip -= 1
                continue

            if sp >= 0 and tp >= 0:
                if s[sp] != t[tp]:
                    return False
                sp -= 1
                tp -= 1
            else:
                return False
            
            
        return True