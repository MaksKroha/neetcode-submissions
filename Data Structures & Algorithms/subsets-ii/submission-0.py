class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def backtrack(curr_arr, idx):
            result.append(curr_arr.copy())

            if idx == len(nums):
                return 

            counter = idx
            while counter < len(nums):
                if counter == idx or nums[counter] != nums[counter - 1]:
                    curr_arr.append(nums[counter])
                    backtrack(curr_arr, counter + 1)
                    curr_arr.pop()
                counter += 1
        backtrack([], 0)
        return result
                
        