class Solution:
    def partition(self, s: str) -> List[List[str]]:
        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        
        for j in range(len(s) - 1, -1, -1):
            for i in range(j, len(s)):
                if i == j:
                    is_palindrome[j][i] = True
                elif j + 1 == i:
                    is_palindrome[j][i] = s[j] == s[i]
                else:
                    is_palindrome[j][i] = s[j] == s[i] and is_palindrome[j+1][i-1]
        
        result = []
        def backtrack(curr_arr, start_i):
            if start_i == len(s):
                result.append(curr_arr.copy())
                return

            for end_i in range(start_i, len(s)):
                if is_palindrome[start_i][end_i]:
                    curr_arr.append(s[start_i: end_i + 1])
                    backtrack(curr_arr, end_i + 1)
                    curr_arr.pop()
        backtrack([], 0)
        return result

