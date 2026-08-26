class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_boundaries = [len(heights)] * len(heights)
        right_stack = []
        for i in range(len(heights)):
            while right_stack and heights[right_stack[-1]] > heights[i]:
                right_boundaries[right_stack[-1]] = i
                right_stack.pop()
            right_stack.append(i)

        left_boundaries = [-1] * len(heights)
        left_stack = []
        for i in range(len(heights) - 1, -1, -1):
            while left_stack and heights[left_stack[-1]] > heights[i]:
                left_boundaries[left_stack[-1]] = i
                left_stack.pop()
            left_stack.append(i)

        result = -1
        for i, (left, right) in enumerate(zip(left_boundaries, right_boundaries)):
            result = max(result, heights[i] * (right - left - 1))
        return result
