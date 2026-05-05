class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.double_booked = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        overlapping = False
        new_book = [startTime, endTime]
        new_doubles = []
        for booking in self.booked:
            if self.overlaps(booking, new_book):
                overlapping = True
                # bring overlapping part over
                new_doubles.append([max(booking[0], startTime), min(booking[1], endTime)])
        
        if overlapping:
            for booking in self.double_booked:
                if self.overlaps(booking, new_book):
                    return False
            for i in new_doubles:
                self.double_booked.append(i)

        self.booked.append(new_book)
        return True
            

        
    def overlaps(self, a, b):
        if b[0] >= a[1]:
            return False
        if a[0] >= b[1]:
            return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)