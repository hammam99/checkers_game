import os
from board import Board

if __name__ == "__main__":
    b = Board()
    b.print()
    while True:
        print("Enter command or ?: ", end="")
        cmd = input()
        if (cmd == 'quit'):
            break
        elif (cmd == '?'):
            print("Available Commands:")
            print("  quit:")
            print("  move x y dir: dir can be 'left' or 'right' ")
            print("  ?: this message")
        elif ((arr := cmd.split(' '))[0] == 'move'):
            if b.move_checker(arr[1], arr[2], arr[3]):
                # Clears terminal on Windows and UNIX systems
                # to make the program look more interactive
                os.system('cls' if os.name == 'nt' else 'clear')
                b.print()
        else:
            print("Command Not Found: enter ? to list commands")
            continue