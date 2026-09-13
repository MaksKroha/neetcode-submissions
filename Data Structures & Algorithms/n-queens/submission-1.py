class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []  

        columns = [True] * n
        main_diag = [True] * (n * 2 - 1)
        anti_diag = [True] * (n * 2 - 1)

        board = [['.'] * n for _ in range(n)]

        def backtrack(row_i):
            if row_i == n:
                result.append(["".join(row) for row in board])
                return 

            for col_i in range(n):
                if columns[col_i] and \
                    main_diag[row_i - col_i] and \
                    anti_diag[row_i + col_i]:

                    columns[col_i] = False
                    main_diag[row_i - col_i] = False
                    anti_diag[row_i + col_i] = False
                    board[row_i][col_i] = "Q"

                    backtrack(row_i + 1)

                    columns[col_i] = True
                    main_diag[row_i - col_i] = True
                    anti_diag[row_i + col_i] = True
                    board[row_i][col_i] = "."
        backtrack(0)
        return result

