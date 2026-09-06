class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        available = [True] * len(nums)

        def dfs(curr_arr):
            nonlocal result, available

            if len(curr_arr) == len(nums):
                result.append(curr_arr.copy())
                return

            for idx, is_available in enumerate(available):
                if is_available:
                    curr_arr.append(nums[idx])
                    available[idx] = False

                    dfs(curr_arr)

                    curr_arr.pop()
                    available[idx] = True
        dfs([])
        return result