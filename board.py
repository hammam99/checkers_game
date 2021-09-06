P1 = '0'
P2 = 'X'

class Board:
    # This function fills the board with the initial state of a game
    # by using Python list comprehension to produce a 2D-array.
    def __init__(self):
        self.turn = P1
        def fill_cel(x, y):
            # Filling first and last 3 rows with checkers.
            if y < 3 or 7-y < 3:
                rep = P1 if y < 3 else P2
                # The cordinates cannot be of the same type, even or oneven,
                # that is to be noticed by observation of the board.
                # Using a XOR gate to achieve that.
                if (y % 2 == 0) != (x % 2 == 0):
                    return rep
            return "*" # represents empty cell
        self.board = [[fill_cel(x, y) for x in range(8)] for y in range(8)]

    def print(self):
        print(' ', '| ', end='')
        for x in range(8): print(x, ' ', end='')
        print("")
        print(" ", end='')
        for x in range(8): print('---', end='')
        print("")
        for i in range(8):
            print(i, '| ', end='')
            for c in self.board[i]:
                print(c, ' ', end="")
            print("")
        print("It's " + self.turn + "'s turn")
    
    def toggle_turn(self):
        self.turn = P2 if self.turn == P1 else P1
    
    def move_checker(self, x, y, dir):
        tmp = self.board[int(y)][int(x)]

        # check if player is trying to move own checker
        if tmp != self.turn:
            print('Connot move: not your own checker')
            return False

        # check exceeding borders
        if ((self.turn == P1 and int(y) >= 7) or
            (self.turn == P2 and int(y) < 1) or
            (dir == 'right' and int(x) >= 7) or
                (dir == 'left' and int(x) < 1)):
            print('Connot move: exceeded borders')
            return False

        # The operator to use depends on the player and on the direction.
        y_op = 1 if tmp == P1 else -1
        x_op = 1 if dir == 'right' else -1

        dest = self.board[int(y)+y_op][int(x)+x_op]
        if dest == self.turn:
            return False
        elif dest == "*":
            self.board[int(y)+y_op][int(x)+x_op] = tmp
        else:
            # checking whether the attack is possible
            if self.board[int(y)+(y_op*2)][int(x)+(x_op*2)] == "*":
                self.board[int(y)+y_op][int(x)+x_op] = "*"
                self.board[int(y)+(y_op*2)][int(x)+(x_op*2)] = tmp
            else:
                print("cannot move")
                return False

        # toggle turn and change current cell after successvol move
        self.board[int(y)][int(x)] = "*"
        self.toggle_turn()
        return True
