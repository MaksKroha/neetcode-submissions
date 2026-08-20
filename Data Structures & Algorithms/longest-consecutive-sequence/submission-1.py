class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                counter = 1
                while num + counter in nums_set:
                    counter += 1

                longest = max(longest, counter)
        return longest
            
                
