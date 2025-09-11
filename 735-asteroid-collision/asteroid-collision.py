class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while rock < 0:
                if not stack:
                    stack.append(rock)
                    break
                if stack[-1] > 0:
                    diff = stack[-1] + rock
                    if diff > 0:
                        break
                    elif diff == 0:
                        stack.pop()
                        break
                    else:
                        stack.pop()
                        continue
                else:
                    stack.append(rock)
                    break
            if rock > 0:
                stack.append(rock)
        return stack