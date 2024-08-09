class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            s = set()
            # Check if numbers 1 to 9 are present
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] < 1 or grid[i + x][j + y] > 9:
                        return False
                    s.add(grid[i + x][j + y])
            if len(s) < 9:
                return False
        
            # Check sum of rows, columns, and diagonals
            row1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
            row2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
            row3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
        
            col1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
            col2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
            col3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
        
            diag1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            diag2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
        
            return row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count

        
