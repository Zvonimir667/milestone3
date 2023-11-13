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
    
    def place_ships(self):
        """
        Place ships on the board
        """
        for ship, size in self.ships.items():
            self.place_ship(ship, size)

    def place_ship(self, ship, size):
        """
        Place a single ship on the game board.
        """
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - size)
                if all(self.board[row][col + i] == 'O' for i in range(size)):
                    for i in range(size):
                        self.board[row][col + i] = 'S'  # 'S' represents a ship
                    break
            else:
                row = random.randint(0, self.size - size)
                col = random.randint(0, self.size - 1)
                if all(self.board[row + i][col] == 'O' for i in range(size)):
                    for i in range(size):
                        self.board[row + i][col] = 'S'
                    break