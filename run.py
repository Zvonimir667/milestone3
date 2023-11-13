import random

class BattleshipGame:
    def board(self, size=5):
        """
        Initialize the Battleship game with an empty board
        """
        self.size = size
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

    def print_board(self, hide_ship=False):
        """
        Print the game board, hiding ships on the board
        """
        for row in self.board:
            print(' '.join(['X' if cell == 'S' and hide_ships else cell for cell in row]))
        print()
    
    