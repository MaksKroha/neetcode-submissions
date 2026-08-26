from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)
        non_zeros = len(letters)
        left, right = 0, 0

        if len(s1) > len(s2):
            return False
        
        while right < len(s1):
            if s2[right] in letters:
                if letters[s2[right]] == 0:
                    non_zeros += 1
                letters[s2[right]] -= 1
                if letters[s2[right]] == 0:
                    non_zeros -= 1
            else:
                non_zeros += 1
                letters[s2[right]] = -1
            right += 1
        if non_zeros == 0:
            return True
        
        while right < len(s2):
            letters[s2[left]] += 1
            if letters[s2[left]] == 0:
                non_zeros -= 1
            elif letters[s2[left]] == 1:
                non_zeros += 1

            if s2[right] in letters:
                if letters[s2[right]] == 0:
                    non_zeros += 1
                letters[s2[right]] -= 1
                if letters[s2[right]] == 0:
                    non_zeros -= 1
            else:
                non_zeros += 1
                letters[s2[right]] = -1
            if non_zeros == 0:
                return True
            
            left += 1
            right += 1
        return False
