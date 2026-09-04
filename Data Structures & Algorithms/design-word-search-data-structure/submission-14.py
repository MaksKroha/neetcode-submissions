from collections import deque
from functools import reduce

class WordDictionary:
    def __init__(self):
        self.children: dict[str, WordDictionary] = {}
        self.is_word: bool = False

    def addWord(self, word: str) -> None:
        curr_dict = self
        for symbol in word:
            if symbol in curr_dict.children:
                curr_dict = curr_dict.children[symbol] 
            else:
                new_dict = WordDictionary()
                curr_dict.children[symbol] = new_dict
                curr_dict = new_dict
        curr_dict.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, start_idx):
            if start_idx == len(word):
                return node.is_word

            if word[start_idx] != '.' and \
                word[start_idx] not in node.children:
                return False
            
            if word[start_idx] == '.':
                for child in node.children.values():
                    if dfs(child, start_idx + 1):
                        return True
            else:
                if dfs(node.children[word[start_idx]], start_idx + 1):
                    return True
            return False   
        return dfs(self, 0)
         

