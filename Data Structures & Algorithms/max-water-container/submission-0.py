class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        best_score = -1
        while left < right:
            best_score = max(
                best_score,
                (right - left) * min(
                    heights[left],
                    heights[right]
                )
            )

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best_score