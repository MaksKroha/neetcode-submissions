class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available = {}
        for i, num in enumerate(nums):
            if target - num in available:
                return [
                    min(i, available[target - num]),
                    max(i, available[target - num])
                ]
            else:
                available[num] = i
        

