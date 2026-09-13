import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_largest = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest, val)

        if len(self.k_largest) == self.k + 1:
            heapq.heappop(self.k_largest)
            
        return self.k_largest[0]