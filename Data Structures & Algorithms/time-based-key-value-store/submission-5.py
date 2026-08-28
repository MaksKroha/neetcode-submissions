class TimeMap:

    def __init__(self):
        self.dictionatry = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionatry:
            self.dictionatry[key] = [(timestamp, value)]
        else:
            self.dictionatry[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionatry:
            return ""

        left, right = 0, len(self.dictionatry[key]) - 1
        
        results = []
        while left <= right:
            mid = (left + right) // 2

            if self.dictionatry[key][mid][0] > timestamp:
                right = mid - 1
            else:
                results.append(self.dictionatry[key][mid][1])
                left = mid + 1
        return results[-1] if results else ""
