class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_symbols = {'(': ')', '{': '}', '[': ']'}

        for symbol in s:
            if symbol in open_symbols:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                if open_symbols[stack[-1]] != symbol:
                    return False
                stack.pop()
        return len(stack) == 0