from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr_freq = {key: 0 for key in set(t)}
        dest_freq = Counter(t)
        covered_num = 0
        min_sub_size = 100001
        min_sub_str = ""

        left, right = 0, 0
        while right < len(s) + 1:
            if covered_num == len(curr_freq):
                while covered_num == len(curr_freq):
                    if s[left] in curr_freq:
                        curr_freq[s[left]] -= 1
                        covered_num -= curr_freq[s[left]] < dest_freq[s[left]]
                    left += 1

                if min_sub_size > right - left + 1:
                    min_sub_size = right - left + 1
                    min_sub_str = s[left - 1: right]
            else:
                right += 1
                if right > len(s):
                    break

                if s[right - 1] in curr_freq:
                    curr_freq[s[right - 1]] += 1
                    covered_num += curr_freq[s[right - 1]] == dest_freq[s[right - 1]]
        return min_sub_str