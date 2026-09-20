class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []

        curr_interval = intervals[0]
        for interval in intervals[1:]:
            if curr_interval[1] >= interval[0]:
                curr_interval[1] = max(curr_interval[1], interval[1])
            else:
                result.append(curr_interval)
                curr_interval = interval
        result.append(curr_interval)
        return result
