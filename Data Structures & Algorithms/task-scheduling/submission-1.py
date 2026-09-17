import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()

        counter = [0] * 26
        for task in tasks:
            counter[ord(task) - ord('A')] += 1

        heap = [-freq for freq in counter if freq != 0]
        heapq.heapify(heap)

        time = 0
        while heap or queue:
            if heap:
                el = heapq.heappop(heap)

                if el != -1:
                    queue.appendleft((time, el))
    
            if queue:
                if time - queue[-1][0] == n:
                    _, freq = queue.pop()
                    heapq.heappush(heap, freq + 1)

            time += 1


        return time
            

