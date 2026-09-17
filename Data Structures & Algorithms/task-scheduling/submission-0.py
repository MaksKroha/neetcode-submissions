import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()

        counter = {}
        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1
        
        heap = []
        for task, freq in counter.items():
            heapq.heappush(heap, (-freq, task))

        time = 0
        while heap or queue:
            # print(f"\nstart time = {time}")
            # print(f"heap = {heap}")
            # print(f"queue = {queue}")
            if heap:
                el = heapq.heappop(heap)

                if el[0] != -1:
                    queue.appendleft((time, el))
    
            if queue:
                if time - queue[-1][0] == n:
                    _, (freq, task) = queue.pop()
                    heapq.heappush(heap, (freq + 1, task))

            time += 1


        return time
            

