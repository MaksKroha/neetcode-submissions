import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            stone_1 = heapq.heappop(heap)
            stone_2 = heapq.heappop(heap)

            if stone_1 > stone_2:
                heapq.heappush(heap, stone_2 - stone_1)
            elif stone_1 < stone_2:
                heapq.heappush(heap, stone_1 - stone_2)
        return -heap[0] if heap else 0
