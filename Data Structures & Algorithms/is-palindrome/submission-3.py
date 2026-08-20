class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabetic = set()
        alphabetic.update([chr(i) for i in range(ord('a'), ord('z') + 1)])
        alphabetic.update([chr(i).upper() for i in range(ord('a'), ord('z') + 1)])
        alphabetic.update(str(i) for i in range(10))

        left, right = 0, len(s) - 1
        while left < right:
            while left < len(s) - 1 and s[left] not in alphabetic:
                left += 1
            while right > 0 and s[right] not in alphabetic:
                right -= 1
            
            if left > right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

