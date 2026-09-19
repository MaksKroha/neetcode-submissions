import heapq 


class MedianFinder:
    def __init__(self):
        self.max_heap = [] 
        self.min_heap = []       

    def addNum(self, num: int) -> None:
        if self.max_heap and num < -self.max_heap[0]:
            if len(self.max_heap) - 1 == len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            heapq.heappush(self.max_heap, -num)
        elif self.min_heap and num <= self.min_heap[0]:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if len(self.min_heap) - 1 == len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) - 1 == len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) - 1 == len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        