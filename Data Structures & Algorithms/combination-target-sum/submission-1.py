class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        def dfs(curr_arr, curr_summa, new_idx) -> bool:
            nonlocal result
            if new_idx == len(nums):
                if curr_summa == target:
                    result.append(curr_arr.copy())
                return 
            if curr_summa > target:
                return 

            curr_arr.append(nums[new_idx])
            dfs(curr_arr, curr_summa + nums[new_idx], new_idx)
            curr_arr.pop()
            dfs(curr_arr, curr_summa, new_idx + 1)

        dfs([], 0, 0)
        return result
