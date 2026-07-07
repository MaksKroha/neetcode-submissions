class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        prefix = 1
        for num in nums[:-1]:
            prefix *= num
            result.append(prefix)
        
        suffix = 1
        for i_num in range(len(nums) - 2, -1, -1):
            suffix *= nums[i_num + 1]
            result[i_num] *= suffix
        return result