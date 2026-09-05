class Trie:
    def __init__(self, prefix: str):
        self.prefix: str = prefix
        self.children: dict[str, Trie] = {}
        self.is_word: bool = False

    def add_word(self, word: str):
        curr_trie = self
        
        prefix = ""
        for symbol in word:
            prefix = f"{prefix}{symbol}"
            if symbol in curr_trie.children:
                curr_trie = curr_trie.children[symbol]
            else:
                new_trie = Trie(prefix)
                curr_trie.children[symbol] = new_trie
                curr_trie = new_trie
        curr_trie.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie("")
        for word in words:
            trie.add_word(word)

        result = set()
        visited: dict[tuple[int, int], bool] = {}
        def search_words(i, j, curr_trie):
            nonlocal result, visited
            visited[(i, j)] = True

            if board[i][j] in curr_trie.children:
                next_trie = curr_trie.children[board[i][j]]
                if next_trie.is_word:
                    result.add(next_trie.prefix)

                for i_new, j_new in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if -1 != i_new and i_new != len(board) and \
                        -1 != j_new and j_new != len(board[0]) and \
                        ((i_new, j_new) not in visited or not visited[(i_new, j_new)]):

                        search_words(i_new, j_new, next_trie)
            visited[(i, j)] = False

        for row in range(len(board)):
            for col in range(len(board[0])):
                search_words(row, col, trie)
        return list(result)



