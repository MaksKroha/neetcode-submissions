from collections import deque
from functools import reduce

class WordDictionary:
    def __init__(self, val=""):
        self.val: str = val
        self.children: dict[str, WordDictionary] = {}
        self.is_word: bool = False

    def addWord(self, word: str) -> None:
        curr_dict = self
        for symbol in word:
            if symbol in curr_dict.children:
                curr_dict = curr_dict.children[symbol] 
            else:
                new_dict = WordDictionary(symbol)
                curr_dict.children[symbol] = new_dict
                curr_dict = new_dict
        curr_dict.is_word = True

    def search(self, word: str) -> bool:
        return self.search_2(0, word)

    def search_2(self, start_idx, word) -> bool:
        if start_idx == len(word):
            return self.is_word
        # print(f"{start_idx}  |{word}|")

        if word[start_idx] != '.' and \
            word[start_idx] not in self.children:
            return False
        
        if word[start_idx] == '.':
            for child in self.children.values():
                if child.search_2(start_idx + 1, word):
                    return True
        else:
            if self.children[word[start_idx]].search_2(start_idx + 1, word):
                return True
        return False

