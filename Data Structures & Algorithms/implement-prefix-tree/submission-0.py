class PrefixTree:
    def __init__(self, val=""):
        self.val: str = val
        self.children: dict[string, PrefixTree] = {}
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        curr_tree = self
        for symbol in word:
            if symbol in curr_tree.children:
                curr_tree = curr_tree.children[symbol]
            else:
                new_tree = PrefixTree(symbol)
                curr_tree.children[symbol] = new_tree
                curr_tree = new_tree
        curr_tree.is_word = True


    def search(self, word: str) -> bool:
        curr_tree = self
        for symbol in word:
            if symbol not in curr_tree.children:
                return False
            
            curr_tree = curr_tree.children[symbol]
        return curr_tree.is_word


    def startsWith(self, prefix: str) -> bool:
        curr_tree = self
        for symbol in prefix:
            if symbol not in curr_tree.children:
                return False

            curr_tree = curr_tree.children[symbol]
        return True
        