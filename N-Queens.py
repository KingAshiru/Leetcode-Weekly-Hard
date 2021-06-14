class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = []
        self.queens = set()
        self.solveNQueensHelper(0)
        return self.result
    
    def solveNQueensHelper(self, row):
        if row == self.n:
            self.result.append(self.generateQueens())
        
        for col in range(self.n):
            if self.isSafe(row, col):
                self.queens.add((row, col))
                self.solveNQueensHelper(row + 1)
                self.queens.remove((row, col))
    
    def isSafe(self, row, col):
        for (queenRow, queenCol) in self.queens:
            if queenRow == row or queenCol == col:
                return False
            if abs(queenRow - row) == abs(queenCol - col):
                return False
        return True
    
    def generateQueens(self):
        board = []
        for row in range(self.n):
            boardRow = ''
            for col in range(self.n):
                if (row, col) in self.queens:
                    boardRow += 'Q'
                else:
                    boardRow += '.'
            board.append(boardRow)
        return board
