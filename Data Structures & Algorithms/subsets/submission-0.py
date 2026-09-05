class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curr_stack, idx):
            nonlocal result
            if idx == len(nums):
                result.append(curr_stack.copy())
                return

            curr_stack.append(nums[idx])
            backtrack(curr_stack, idx + 1)
            curr_stack.pop()
            backtrack(curr_stack, idx + 1)
        backtrack([], 0)
        
        return result 
