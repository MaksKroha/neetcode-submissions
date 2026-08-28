import heapq   
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)

        result = []
        for right in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            while heap[0][1] < right - k + 1:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
