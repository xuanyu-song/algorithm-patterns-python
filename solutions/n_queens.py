"""N-Queens (LeetCode 51). Place one queen per row and undo invalid branches."""

class Solution:

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.res = []
        chessboard = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append('.')
            chessboard.append(temp)
        self.backtracking(0, chessboard, n)
        return self.res

    def isValid(self, n, row, col, chessboard):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        i, j = (row - 1, col - 1)
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = (row - 1, col + 1)
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(self, row, chessboard, n):
        if row >= n:
            temp_res = []
            for temp in chessboard:
                temp_res.append(''.join(temp))
            self.res.append(temp_res)
            return
        for col in range(n):
            if self.isValid(n, row, col, chessboard):
                chessboard[row][col] = 'Q'
                self.backtracking(row + 1, chessboard, n)
                chessboard[row][col] = '.'
