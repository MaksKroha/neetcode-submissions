import heapq
import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = lambda x, y: math.sqrt(x**2 + y**2)
        
        for point in points:
            if len(heap) == k:
                distance = -dist(*point)
                if heap[0][0] < distance:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (distance, point))
            else:
                distance = -dist(*point)
                heapq.heappush(heap, (distance, point))
        return [el[1] for el in heap]
                
