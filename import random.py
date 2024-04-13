import random

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
    
    def print(self):
        for row in self.grid:
            print(' '.join(row))
    
    def place_ship(self, ship):
        x, y, orientation = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal' and x + ship.size <= self.size:
            for i in range(ship.size):
                self.grid[y][x + i] = 'O'
            return True
        elif orientation == 'vertical' and y + ship.size <= self.size:
            for i in range(ship.size):
                self.grid[y + i][x] = 'O'
            return True
        else:
            return self.place_ship(ship)
    
    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
    
    def is_ship(self, x, y):
        return self.grid[y][x] == 'O'
    
    def is_hit(self, x, y):
        return self.grid[y][x] == 'X'
    
    def mark_hit(self, x, y):
        self.grid[y][x] = 'X'
    
    def mark_miss(self, x, y):
        self.grid[y][x] = '-'

class Ship:
    def __init__(self, size):
        self.size = size

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board(10)
        self.ships = [Ship(5), Ship(4), Ship(3), Ship(3), Ship(2)]
    
    def place_ships(self):
        for ship in self.ships:
            while not self.board.place_ship(ship):
                pass

    def make_move(self, other_board):
        x, y = random.randint(0, 9), random.randint(0, 9)
        while other_board.is_hit(x, y) or other_board.is_miss(x, y):
            x, y = random.randint(0, 9), random.randint(0, 9)
        if other_board.is_ship(x, y):
            print(f"{self.name} hits at {chr(x + 65)}{y + 1}!")
            other_board.mark_hit(x, y)
        else:
            print(f"{self.name} misses at {chr(x + 65)}{y + 1}.")
            other_board.mark_miss(x, y)

def main():
    print("Welcome to Battleship!")
    player1 = Player("Player 1")
    player2 = Player("Player 2 (Computer)")
    player1.place_ships()
    player2.place_ships()
    while True:
        print("\nPlayer 1 Board:")
        player1.board.print()
        print("\nPlayer 2 Board:")
        player2.board.print()
        player1.make_move(player2.board)
        if all(ship.size == 0 for ship in player2.ships):
            print("Player 1 wins!")
            break
        player2.make_move(player1.board)
        if all(ship.size == 0 for ship in player1.ships):
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    main()
