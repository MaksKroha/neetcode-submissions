from io import StringIO


class Solution:
    def encode(self, strs: List[str]) -> str:
        result_string = StringIO()
        for string in strs:
            result_string.write(f"{len(string)}|{string}")
        return result_string.getvalue()



    def decode(self, s: str) -> List[str]:
        result_arr = []
        left, right = 0, 0

        while right < len(s):
            while s[right] != '|':
                right += 1

            new_right = right + int(s[left: right]) + 1
            result_arr.append(s[right + 1: new_right])

            left = right = new_right
        return result_arr


