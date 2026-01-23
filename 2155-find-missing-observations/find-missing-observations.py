class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls))
        
        m_total = 0

        for roll in rolls:
            m_total += roll

        n_total = total - m_total

        if n_total < n or n_total > n*6:
            return []

        res = [1 for i in range(n)]
        n_total -= n

        i = 0
        while i < n and n_total > 0:
            if n_total >= 5:
                res[i] += 5
                n_total -= 5
            else:
                res[i] += n_total
                n_total -= n_total
            i += 1
        
        return res