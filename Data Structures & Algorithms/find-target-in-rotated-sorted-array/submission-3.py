class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                if target >= nums[left]:
                    right = mid - 1
                else:
                    if nums[left] > nums[mid]:
                        left += 1
                        right = mid - 1
                    else:
                        left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                if nums[right] >= target:
                    left = mid + 1
                else:
                    if nums[right] < nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
            