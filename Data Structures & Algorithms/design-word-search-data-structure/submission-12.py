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
        curr_dict_queue = deque([self])
        for symbol in word:
            if not curr_dict_queue:
                return False

            if symbol == '.':
                for _ in range(len(curr_dict_queue)):
                    curr_dict = curr_dict_queue.popleft()
                    curr_dict_queue.extend(curr_dict.children.values())
            else:
                for _ in range(len(curr_dict_queue)):
                    curr_dict = curr_dict_queue.popleft()
                    if symbol in curr_dict.children:
                        curr_dict_queue.append(curr_dict.children[symbol])
        return len(curr_dict_queue) != 0 and reduce(
            lambda res, el: res and el.is_word,
            curr_dict_queue, True
        )
