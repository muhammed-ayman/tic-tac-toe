import tkinter as tk
from tkinter import messagebox
from typing import List, Optional

class Player:
    """
    Represents a player in the Tic-Tac-Toe game.
    """
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

class Board:
    """
    Represents the game board for Tic-Tac-Toe.
    """
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def check_winner(self) -> str:
        """
        Checks if there is a winner on the board.
        Returns the winning player's symbol or "Draw" if it's a draw.
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0] + " Win!"  # Horizontal win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i] + " Win!"  # Vertical win

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0] + " Win!"  # Diagonal win
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2] + " Win!"  # Diagonal win

        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            return "Draw"
        return ""

    def is_position_empty(self, row: int, column: int) -> bool:
        """
        Checks if a given position on the board is empty.
        """
        return self.board[row][column] == " "

    def make_move(self, row: int, column: int, player: Player) -> None:
        """
        Makes a move on the board by placing the player's symbol at the specified position.
        """
        self.board[row][column] = player.symbol

class TicTacToeGame:
    """
    Represents the Tic-Tac-Toe game.
    """
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.players: List[Player] = []
        self.current_player_index: int = 0
        self.board = Board()
        self.buttons: List[tk.Button] = []

    def create_button(self, row: int, column: int) -> None:
        """
        Creates a button at the specified row and column on the game board.
        """
        button = tk.Button(
            self.window,
            text=" ",
            width=10,
            height=5,
            command=lambda: self.handle_button_click(button, row, column)
        )
        button.grid(row=row, column=column)
        self.buttons.append(button)

    def create_board(self) -> None:
        """
        Creates the game board by creating buttons for each position.
        """
        self.clear_player_input_screen()

        for row in range(3):
            for column in range(3):
                self.create_button(row, column)

    def add_player(self, name: str, symbol: str) -> None:
        """
        Adds a player to the game.
        """
        player = Player(name, symbol)
        self.players.append(player)

    def switch_player(self) -> None:
        """
        Switches the current player to the next player.
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def update_button_text(self, button: tk.Button, row: int, column: int) -> None:
        """
        Updates the text on the button based on the game board state.
        """
        button["text"] = self.board.board[row][column]

    def handle_button_click(self, button: tk.Button, row: int, column: int) -> None:
        """
        Handles the button click event and updates the game state accordingly.
        """
        if self.board.is_position_empty(row, column):
            player = self.players[self.current_player_index]
            self.board.make_move(row, column, player)
            self.update_button_text(button, row, column)
            result = self.board.check_winner()
            if result:
                messagebox.showinfo("Game Result", result)
                self.reset_game()
            else:
                self.switch_player()

    def clear_player_input_screen(self) -> None:
        """
        Clears the player input screen.
        """
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_player_input_screen(self) -> None:
        """
        Shows the player input screen where players can enter their names and symbols.
        """
        self.clear_player_input_screen()

        player1_label = tk.Label(self.window, text="Player 1")
        player1_label.grid(row=0, column=0, padx=5, pady=5)
        player1_name_label = tk.Label(self.window, text="Name:")
        player1_name_label.grid(row=1, column=0, padx=5, pady=5)
        player1_name_entry = tk.Entry(self.window)
        player1_name_entry.grid(row=1, column=1, padx=5, pady=5)
        symbol1_label = tk.Label(self.window, text="Symbol (X/O):")
        symbol1_label.grid(row=2, column=0, padx=5, pady=5)
        symbol1_entry = tk.Entry(self.window)
        symbol1_entry.grid(row=2, column=1, padx=5, pady=5)

        player2_label = tk.Label(self.window, text="Player 2")
        player2_label.grid(row=3, column=0, padx=5, pady=5)
        player2_name_label = tk.Label(self.window, text="Name:")
        player2_name_label.grid(row=4, column=0, padx=5, pady=5)
        player2_name_entry = tk.Entry(self.window)
        player2_name_entry.grid(row=4, column=1, padx=5, pady=5)
        symbol2_label = tk.Label(self.window, text="Symbol (X/O):")
        symbol2_label.grid(row=5, column=0, padx=5, pady=5)
        symbol2_entry = tk.Entry(self.window)
        symbol2_entry.grid(row=5, column=1, padx=5, pady=5)

        start_button = tk.Button(
            self.window,
            text="Start Game",
            command=lambda: self.start_game(
                player1_name_entry.get(),
                symbol1_entry.get(),
                player2_name_entry.get(),
                symbol2_entry.get()
            )
        )
        start_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def validate_player_input(self, player1_name: str, symbol1: str, player2_name: str, symbol2: str) -> bool:
        """
        Validates the player input and checks if it's valid.
        """
        player1_name = player1_name.strip()
        symbol1 = symbol1.strip().upper()
        player2_name = player2_name.strip()
        symbol2 = symbol2.strip().upper()

        if not player1_name or not symbol1 or not player2_name or not symbol2:
            messagebox.showerror("Error", "All fields must be filled!")
            return False
        if symbol1 != "X" and symbol1 != "O":
            messagebox.showerror("Error", "Symbol for Player 1 must be 'X' or 'O'!")
            return False
        if symbol2 != "X" and symbol2 != "O":
            messagebox.showerror("Error", "Symbol for Player 2 must be 'X' or 'O'!")
            return False
        if symbol1 == symbol2:
            messagebox.showerror("Error", "Symbols for Player 1 and Player 2 must be different!")
            return False

        self.add_player(player1_name, symbol1)
        self.add_player(player2_name, symbol2)
        return True

    def start_game(self, player1_name: str, symbol1: str, player2_name: str, symbol2: str) -> None:
        """
        Starts the game by validating player input and creating the game board.
        """
        if self.validate_player_input(player1_name, symbol1, player2_name, symbol2):
            self.create_board()

    def reset_game(self) -> None:
        """
        Resets the game by clearing the board and showing the player input screen again.
        """
        self.board = Board()
        for button in self.buttons:
            button.destroy()
        self.buttons = []
        self.show_player_input_screen()

    def run(self) -> None:
        """
        Runs the Tic-Tac-Toe game.
        """
        self.show_player_input_screen()
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
