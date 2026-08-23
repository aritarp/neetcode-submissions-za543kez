class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        # check if the new event overlaps with any existing event
        for s,e in self.events:
            if startTime < e and s < endTime:
                return False
        self.events.append((startTime,endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)