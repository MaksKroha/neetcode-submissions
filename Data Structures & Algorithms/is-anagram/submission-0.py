class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_symbols = {}
        for symbol in s:
            s_symbols[symbol] = s_symbols.get(symbol, 0) + 1
        
        for symbol in t:
            if symbol not in s_symbols:
                return False
    
            s_symbols[symbol] -= 1
            if s_symbols[symbol] == 0:
                del s_symbols[symbol]
        return len(s_symbols) == 0