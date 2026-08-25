class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = {symbol: False for symbol in set(s)}
        max_len = 0
        
        left = 0
        for right in range(len(s)):
            if repeated[s[right]]:
                while s[left] != s[right]:
                    repeated[s[left]] = False
                    left += 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
                repeated[s[right]] = True
        return max_len