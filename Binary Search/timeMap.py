class TimeMap:

    def __init__(self):
        self.hashed_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashed_map:
            self.hashed_map[key] = []
            self.hashed_map[key].append([timestamp, value])
        else:
            self.hashed_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashed_map:
            return ""
        left = 0
        right = len(self.hashed_map[key])-1
        closest = ""
        while left <= right:
            middle = ((right - left) // 2) + left
            if self.hashed_map[key][middle][0] > timestamp:
                right = middle - 1
            elif self.hashed_map[key][middle][0] < timestamp:
                closest = self.hashed_map[key][middle][1]
                left = middle + 1
            elif self.hashed_map[key][middle][0] == timestamp:
                return self.hashed_map[key][middle][1]
        return closest