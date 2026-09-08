class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr_arr, open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(curr_arr))
                return 
            
            if open_count != n:
                curr_arr.append('(')
                backtrack(curr_arr, open_count + 1, close_count)
                curr_arr.pop()
            if close_count < open_count:
                curr_arr.append(')')
                backtrack(curr_arr, open_count, close_count + 1)
                curr_arr.pop()
        backtrack([], 0, 0)
        return result