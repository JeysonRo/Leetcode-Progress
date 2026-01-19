
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for i in range(n)]

        res = 0
        postlist = 0
        for i, question in enumerate(questions):
            res = max(res, dp[i])
            if i + question[1] + 1 >= n:
                postlist = max(res + question[0], postlist)
            else:
                dp[i + question[1] + 1] = max(res + question[0], dp[i + question[1] + 1])

        res = max(res, postlist)
        return res