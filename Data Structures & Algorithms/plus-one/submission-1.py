class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reminder = 0
        
        digits[-1] += 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + reminder 

            result.append(total % 10)
            reminder = total // 10

        if reminder != 0:
            result.append(reminder)
        return result[::-1]