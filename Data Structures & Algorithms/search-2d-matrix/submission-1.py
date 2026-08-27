class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            center = (left + right) // 2  
            center_el = matrix[center // cols][center % cols]  
            if center_el < target:
                left = center + 1 
            elif center_el > target:
                right = center - 1
            else:
                return True
        return False