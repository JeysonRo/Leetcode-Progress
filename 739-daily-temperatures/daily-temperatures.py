class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(temperatures))]

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                temp, index = stack.pop()
                answer[index] = i - index
            stack.append((v, i))
        return answer