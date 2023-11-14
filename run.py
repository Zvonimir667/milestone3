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

    def take_shot(self, guess):
        """
        Take a shot at the specified location on the game board
        """
        row, col = guess
        if self.board[row][col] == 'S':
            hit_ship = self.get_ship_name(row, col)
            self.board[row][col] = 'X'  # 'X' represents a hit
            print(f"Hit! The computer hit your {hit_ship}")
            return True
        elif self.board[row][col] == 'O':
            self.board[row][col] = '/'
            print("Computer Missed!")
            return False

    def get_ship_name(self, row, col):
        """
        Get the name of the ship at the specified location
        """
        for ship, size in self.ships.items():
            if self.is_ship_hit(row, col, ship, size):
                return ship

    def is_ship_hit(self, row, col, ship, size):
        """
        Check if a ship is hit
        """
        if all(0 <= row < self.size and 0 <= col + i < self.size and self.board[row][col + i] == 'X' for i in range(size)):
            return True
        elif all(0 <= row + i < self.size and 0 <= col < self.size and self.board[row + i][col] == 'X' for i in range(size)):
            return True
        return False

    def get_user_guess():
        """
        Get the user's guess for a shot
        """
        while True:
        try:
            guess = input("Enter your guess (row and column, separated by a space): ").split()
            guess = [int(coord) for coord in guess]
            return guess
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")
        
def play_battleship():
    """
    Play the Battleship game with the user and computer taking turns
    """
    game = BattleshipGame()
    game.place_ships()
    computer = BattleshipGame()
    computer.place_ships()
    user_attempts = 0
    computer_attempts = 0

    while any('S' in row for row in computer.board) and any('S' in row for row in game.board):
        print("\nYour Board:")
        game.print_board()
        user_guess = get_user_guess()
        if not (0 <= user_guess[0] < game.size and 0 <= user_guess[1] < game.size):
            print("Invalid guess. Please enter valid row and column values.")
            continue

        if game.take_shot(user_guess):
            user_attempts += 1

        print("\nComputer's Board:")
        computer.print_board(hide_ships=True)
        computer_guess = [random.randint(0, game.size - 1), random.randint(0, game.size - 1)]
        if computer.take_shot(computer_guess):
            computer_attempts += 1

    if all('S' not in row for row in computer.board):
        print("\nCongratulations! You won the game!.")
    else:
        print("\nSorry, the computer won. Better luck next time!")

    print(f"\nYour Attempts: {user_attempts}")
    print(f"Computer's Attempts: {computer_attempts}")

if __name__ == "__main__":
    play_battleship()