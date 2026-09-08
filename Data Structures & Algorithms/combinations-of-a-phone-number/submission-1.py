class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        keypad: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []

        def backtrack(curr_arr, idx):
            if idx == len(digits):
                result.append("".join(curr_arr))
                return

            for symbol in keypad[digits[idx]]:
                curr_arr.append(symbol)
                backtrack(curr_arr, idx + 1)
                curr_arr.pop()
        backtrack([], 0)
        return result