class Solution:
    def totalNQueens(self, n: int):
        self.n = n
        self.count = 0
        self.queens = set()
        self.solveNQueensHelper(0)
        return self.count
    
    def solveNQueensHelper(self, row):
        if row == self.n:
            self.count += 1
        
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
    
    
