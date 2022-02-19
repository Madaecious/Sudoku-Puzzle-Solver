#########################################################################################
# Sudoku Puzzle Solver via Backtracking Algorithm
# -------------------------------------------------------
# Mark Barros
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
#########################################################################################


# This is an import for reading csv files. ----------------------------------------------
import csv

# This looks for blank cells. -----------------------------------------------------------
# Note: Blank cells are represented by zeros
def findNextCellToFill(grid, i, j):
        for x in range(i, 9):
                for y in range(j, 9):
                        if grid[x][y] == 0:
                                return x, y
        for x in range(0, 9):
                for y in range(0, 9):
                        if grid[x][y] == 0:
                                return x, y
        return -1, -1

# This checks for the validity in the context or the row, column, and 3x3 grid. ---------
def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # Find the top left x,y coordinates of the
                        # section containing the i,j cell.
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) 
                        for x in range(secTopX, secTopX + 3):
                                for y in range(secTopY, secTopY + 3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False


# This solves the Sudoku puzzle. --------------------------------------------------------
def solveSudoku(grid, i = 0, j = 0):
        i, j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1, 10):
                if isValid(grid, i, j, e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking purposes:
                        grid[i][j] = 0
        return False


# This is the driver code. --------------------------------------------------------------
if __name__ == "__main__":

        # This opens the input file as a csv.
        input_file = open('input.txt', 'r')
        reader = csv.reader(input_file)

        # This will receive the input values and contain the final solution.
        values = []

        # This reads in the values from the csv file.
        for row in reader:
                values.append(row)
        
        # This converts the values from characters to integers.
        values = [[int(int(j)) for j in i] for i in values]

        # This outputs the Sudoku puzzle.
        print("----------------------------------------------------")
        print("Sudoku Puzzle Solver - By Mark Barros")
        print("----------------------------------------------------")
        print("Original Puzzle:\n")
        for s in values:
                print("\t", *s)
        print("\nSolving Puzzle...")

        # This calls the Sudoku solver.
        solveSudoku(values)

        # This outputs the solution to the console.
        print()
        for s in values:
                print("\t", *s)
        print()
        print("----------------------------------------------------")

# End of Script #########################################################################