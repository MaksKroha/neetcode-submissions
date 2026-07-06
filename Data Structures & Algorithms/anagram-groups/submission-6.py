from functools import reduce

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict[str, list[str]] = {}
        for string in strs:
            frequency = [0] * 26
            for symbol in string:
                frequency[ord(symbol) - ord('a')] += 1
            
            str_arr = ",".join(map(str, frequency))
            if str_arr in result:
                result[str_arr].append(string)
            else:
                result[str_arr] = [string]
        return list(result.values())

