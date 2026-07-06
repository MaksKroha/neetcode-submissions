from functools import reduce

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict[str, list[str]] = {}
        for string in strs:
            frequency = [0] * 26
            for symbol in string:
                frequency[ord(symbol) - ord('a')] += 1
                print(frequency)
            
            str_arr = ",".join(map(str, frequency))
            print(f"{string} = {str_arr} = {hash(str_arr)}")
            if str_arr in result:
                result[str_arr].append(string)
            else:
                result[str_arr] = [string]
        return list(result.values())

