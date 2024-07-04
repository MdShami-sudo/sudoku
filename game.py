import tkinter as tk
from tkinter import messagebox
import random

# Funny emojis to represent numbers 1 to 9
emojis = ["😀", "😂", "😅", "😆", "😎", "😍", "😜", "😲", "😴"]

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku with Emojis")
        self.board = self.create_board()
        self.create_widgets()

    def create_board(self):
        # Simple predefined board for demonstration purposes
        return [
            [0, 2, 0, 4, 0, 6, 0, 8, 0],
            [0, 0, 3, 0, 0, 0, 7, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 3, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 8, 0, 0, 0, 4, 0, 0],
            [0, 7, 0, 9, 0, 2, 0, 1, 0]
        ]

    def create_widgets(self):
        self.entries = {}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    value = emojis[self.board[i][j] - 1]
                    entry = tk.Entry(self.root, width=2, font=('Helvetica', 18), justify='center', state='readonly')
                    entry.insert(0, value)
                else:
                    entry = tk.Entry(self.root, width=2, font=('Helvetica', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[(i, j)] = entry
        
        self.check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        self.check_button.grid(row=9, column=4, pady=10)

    def check_solution(self):
        self.update_board_from_entries()
        if self.is_valid_solution():
            messagebox.showinfo("Sudoku", "Congratulations! You solved the Sudoku!")
        else:
            messagebox.showerror("Sudoku", "Oops! There are some mistakes. Try again.")

    def update_board_from_entries(self):
        for i in range(9):
            for j in range(9):
                entry_value = self.entries[(i, j)].get()
                if entry_value in emojis:
                    number = emojis.index(entry_value) + 1
                else:
                    number = 0
                self.board[i][j] = number

    def is_valid_solution(self):
        def is_valid_row(row):
            numbers = [num for num in row if num != 0]
            return len(numbers) == len(set(numbers))

        def is_valid_col(col):
            numbers = [num for num in col if num != 0]
            return len(numbers) == len(set(numbers))

        def is_valid_square(square):
            numbers = [num for num in square if num != 0]
            return len(numbers) == len(set(numbers))

        for i in range(9):
            row = [self.board[i][j] for j in range(9)]
            col = [self.board[j][i] for j in range(9)]
            if not is_valid_row(row) or not is_valid_col(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid_square(square):
                    return False

        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
