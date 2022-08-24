# https://leetcode.com/problems/my-calendar-i/
# https://leetcode.com/problems/my-calendar-i/discuss/2372304/Python-oror-Detailed-Explanation-oror-Easy-Understand-oror-No-Libray-oror-Binary-Search

class MyCalendar:
    def __init__(self):
        self.calendar = []
		# Use Linked List instead, much more faster
		# self.calender = collections.deque()

    def book(self, start: int, end: int) -> bool:
        right = len(self.calendar)
        if right == 0:
            self.calendar.append((start, end))
            return True

        left = 0
        while left < right:
            mid = int(left + (right - left)/2)
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == len(self.calendar):
            self.calendar.append((start, end))
            return True
                
        if self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True
            
        return False


booking_list = [[10,20],[15,25],[20,30]]
result = []
myCalendar = MyCalendar()
for x in booking_list:
    result.append(myCalendar.book(x[0], x[1]))
print(result)
