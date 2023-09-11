import re
from moves import *

branch_counter = 0


WHITE = "white"
BLACK = "black"


class Branch:
    def __init__(self, title, parent=None):
        global branch_counter
        self.name = f"{title} branch {branch_counter}"
        self.parent = parent
        branch_counter += 1
        # copy moves from parent if parent
        if parent:
            self.moves = parent.moves.copy()
            self.next_one = parent.next_one
        else:
            self.moves = []
            self.next_one = WHITE
        print(f"Created {self.name}")

    def get_name(self):
        return self.name

    def add_moves(self, moves: str):
        # print(f"Adding {moves}")
        # split moves on regex "digits with dot", keeping the number as a separate variable
        moves_list = re.split(r" *(\d+\.) *", moves)
        # remove empty ones
        moves_list = [move for move in moves_list if move.strip()]

        # print(f"Moves list: {moves_list}")
        current_move_number = 0
        for move in moves_list:
            move = move.strip()
            # if matches digit with dot, then it's a move number
            if re.match(r"\d+\.", move):
                current_move_number = int(move[:-1])
                continue
            # if not, then it's a move
            # if there is a space in the middle, split into white and black moves
            if " " in move:
                print(move)
                white_move, black_move = move.split()

                # if white move is .. means this is a black variant
                # so let's remove the last move from the list
                if white_move == "..":
                    # if last one was the same number and black, then remove it
                    if self.moves[-1].startswith(f"{current_move_number} black"):
                        self.moves.pop()
                        self.next_one = BLACK
                else:
                    white_move = translate_move(white_move)
                    self.moves.append(
                        f"{current_move_number} white {white_move}")

                black_move = translate_move(black_move)
                self.moves.append(f"{current_move_number} black {black_move}")
                continue
            # single move no color
            move = translate_move(move)
            self.moves.append(f"{current_move_number} white {move}")
        # print(f"Moves list: {self.moves}")

    def set_name(self, comment):
        print(f"Setting name {comment}")
        self.name += " " + comment.strip()


def printBranch(branch, voicer):
    moves = branch.moves
    spoken_text = branch.get_name() + PAUSE + '. '.join(moves) + '.'
    print("Printing: " + branch.get_name())
    voicer.speak(branch.get_name(), spoken_text)
