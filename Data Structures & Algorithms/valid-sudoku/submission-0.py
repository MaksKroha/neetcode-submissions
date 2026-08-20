class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        print(squares)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue 
                    
                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in columns[col]:
                    return False 
                if board[row][col] in squares[3 * (row // 3) + col // 3]:
                    return False

                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[3 * (row // 3) + col // 3].add(board[row][col])
        return True