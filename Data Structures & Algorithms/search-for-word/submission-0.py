class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def is_present(j, i, idx):
            if board[j][i] == "#":
                return False

            prev_val = board[j][i]
            board[j][i] = "#"
            if word[idx] == prev_val:
                if idx + 1 == len(word):
                    return True

                possible_pairs = [(j+1, i), (j-1, i), (j, i+1), (j, i-1)]
                for new_j, new_i in possible_pairs:
                    if 0 <= new_j and new_j < len(board) and \
                        0 <= new_i and new_i < len(board[0]) and \
                        idx + 1 != len(word) and \
                        is_present(new_j, new_i, idx + 1):
                        return True
            board[j][i] = prev_val
            return False
        for j in range(len(board)):
            for i in range(len(board[0])):
                if is_present(j, i, 0):
                    return True
        return False
                    

