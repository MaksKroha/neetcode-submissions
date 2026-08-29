class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        half = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left = float("-inf") if i == 0 else nums1[i - 1]
            nums1_right = float("inf") if i == m else nums1[i]

            nums2_left = float("-inf") if j == 0 else nums2[j - 1]
            nums2_right = float("inf") if j == n else nums2[j]

            if nums1_left > nums2_right:
                right = i - 1
            elif nums2_left > nums1_right:
                left = i + 1
            else:
                max_left = max(nums1_left, nums2_left)
                min_right = min(nums1_right, nums2_right)

                if (m + n) % 2 == 1:
                    return max_left
                return (max_left + min_right) / 2