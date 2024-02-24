import tkinter
import time

SquareSize = 50

# Recursively solve n queens problem
def solveQueensProblem(board, row, gui=None):
    # Return true once all rows covered (all queens placed)
    if row == len(board):
        return True

    # For each column in the current row check
    for column in range(len(board)):
        if isMoveSafe(board, row, column):
            # Once safe, place queen
            board[row][column] = 1
            # If gui given, update the board
            if gui:
                gui.refresh(board)
                gui.update_idletasks()
                time.sleep(0.05)
            # Recursively solve for the next row
            if solveQueensProblem(board, row + 1, gui):
                return True
            # If no solution, go back and remove queen
            board[row][column] = 0

    # If no solution for current row, return false
    return False

# Check if the queen is safe
def isMoveSafe(board, row, column):
    # If there is queen in each column (also for same row), return false
    for i in range(row):
        if board[i][column] == 1:
            return False

    # If there is queen diagonally moving down left
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    # If there is queen diagonally moving up right
    for i, j in zip(range(row, -1, -1), range(column, len(board), 1)):
        if board[i][j] == 1:
            return False

    # Return true if the queen based checks
    return True

class QueensGUI(tkinter.Tk):
    # Initialize the GUI with title, canvas for board, no queens placed
    def __init__(self, boardSize):
        super().__init__()
        self.boardSize = boardSize
        self.title(f"{boardSize} Queens Problem")
        self.canvas = tkinter.Canvas(self, width=boardSize * SquareSize, height=boardSize * SquareSize)
        self.canvas.pack()
        self.board = [[0] * self.boardSize for _ in range(self.boardSize)]
        self.initializeBoard()

    # Draw chessboard squares
    def initializeBoard(self):
        # Go through each row and column
        for row in range(self.boardSize):
            for column in range(self.boardSize):
                if (row + column) % 2 == 0:
                    # Light brown for even
                    color = "#f2dab3"
                else:
                    # Dark brown for odd
                    color = "#b58863"

                # Coordinates of squares using the column and row
                x0, y0 = column * SquareSize, row * SquareSize
                x1, y1 = x0 + SquareSize, y0 + SquareSize

                # Draw square with the color
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, tags="square")

        # Update the board with any queens
        self.refresh(self.board)

    def refresh(self, board):
        # Remove queens before
        self.canvas.delete("queen")
        # Draw queen if it is set as 1
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 1:
                    self.canvas.create_text(column * SquareSize + SquareSize // 2, row * SquareSize + SquareSize // 2, text="♛", font=("Arial", 38), tags="queen", fill="#494847")

def solve8QueensGui():
    # Initialize 8 by 8 GUI
    gui = QueensGUI(8)
    # Solve using board and GUI
    solveQueensProblem(gui.board, 0, gui)
    # Loop to show board
    gui.mainloop()

# Call to run
solve8QueensGui()
