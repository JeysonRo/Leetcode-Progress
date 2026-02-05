class DetectSquares:

    def __init__(self):
        self.x_points = defaultdict(dict) # x_points[x][y] = count

    def add(self, point: List[int]) -> None:
        x_points = self.x_points
        x = point[0]
        y = point[1]
        if y in x_points[x]:
            x_points[x][y] += 1
        else:
            x_points[x][y] = 1

    def count(self, point: List[int]) -> int:
        x_points = self.x_points

        qx = point[0]
        qy = point[1]

        if qx not in x_points:
            return 0
        res = 0
        for y in x_points[qx].keys():
            width = abs(y - qy)
            if width == 0:
                continue
            x2 = qx - width     
            if x2 in x_points and y in x_points[x2] and qy in x_points[x2]:
                res += x_points[x2][y] * x_points[x2][qy] * x_points[qx][y]

            x2 = qx + width
            if x2 in x_points and y in x_points[x2] and qy in x_points[x2]:
                res += x_points[x2][y] * x_points[x2][qy] * x_points[qx][y]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)