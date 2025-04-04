class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        visited = set()

        def visit(room):
            if room in visited:
                return
            
            visited.add(room)

            for i in rooms[room]:
                visit(i)

        visit(0)
        print(visited)
        return n == len(visited)