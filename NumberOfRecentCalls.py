# 933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        self.requests.append(t)
        num = 0
        for req in self.requests:
            if t-3000<=req<=t: num += 1
        return num


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)