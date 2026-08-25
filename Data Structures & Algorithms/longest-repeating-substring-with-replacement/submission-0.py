class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        counter = {symbol: 0 for symbol in set(s)}
        result = 0

        left = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])

            if (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))
        return result
            
        