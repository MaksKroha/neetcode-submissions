class Solution:
    def trap(self, heights: List[int]) -> int:
        left_top_heights = []
        right_top_heights = []

        top_height = 0
        for height in heights:
            left_top_heights.append(top_height)
            top_height = max(top_height, height)
        
        top_height = 0
        for height in heights[::-1]:
            right_top_heights.append(top_height)
            top_height = max(top_height, height)

        result = 0
        for i in range(len(heights)):
            result += max(
                min(
                    left_top_heights[i],
                    right_top_heights[len(heights) - i - 1]
                ) - heights[i],
                0
            )
        return result 
