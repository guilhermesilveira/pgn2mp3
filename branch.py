import re
from moves import translate_move

branch_counter = 0


WHITE = "white"
BLACK = "black"
SHORT_PAUSE = "<break time=\"0.5s\"/>"
LONG_PAUSE = "<break time=\"2.2s\"/>"


def reset_branch_counter():
    global branch_counter
    branch_counter = 0


class Memory:
    memorized = []

    def memorize(self, sequence: str):
        self.memorized.append("," + sequence)

    def read_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            # ignore empty lines or lines with #
            lines = [line.strip() for line in file.readlines()
                     if line.strip() and not line.strip().startswith("#")]
            # invoke memorize for each
            for line in lines:
                self.memorize(line)

    def is_memorized(self, sequence: str):
        for memory in self.memorized:
            if memory.startswith(sequence):
                return True

        return False


def remove_empty(moves_list: list):
    return [move.strip() for move in moves_list if move.strip()]


def get_moves_from_str(moves: str):
    # print(f"Adding {moves}")
    # split moves on regex "digits with dot", keeping the number as a separate variable
    moves_list = re.split(r" *(\d+\.) *", moves)
    # remove empty ones
    moves_list = remove_empty(moves_list)
    return moves_list


class Branch:
    def __init__(self, title, parent=None, memory: Memory = None):
        global branch_counter
        branch_counter += 1
        self.name = f"{title} branch {branch_counter}"
        self.memory = memory
        self.parent = parent
        # copy moves from parent if parent
        if parent:
            self.moves = parent.moves.copy()
            self.next_one = parent.next_one
            self.memorized_so_far = parent.memorized_so_far
            self.full_string = parent.full_string
        else:
            self.moves = []
            self.next_one = WHITE
            self.memorized_so_far = True
            self.full_string = ""

    def move_count(self):
        # length of moves
        return len(self.moves)

    def update_memory(self, move: str):
        self.full_string += f",{move}"
        if not self.memorized_so_far:
            return
        if not self.memory.is_memorized(self.full_string):
            self.memorized_so_far = False

    def get_name(self):
        return self.name

    # if memorized, short pause
    # if not memorized, long pause
    def current_pause(self):
        if self.memorized_so_far:
            return SHORT_PAUSE
        return LONG_PAUSE

    def add_moves(self, moves: str):
        moves_list = get_moves_from_str(moves)

        current_move_number = 0
        for move in moves_list:
            # if matches digit with dot, then it's a move number
            if re.match(r"\d+\.", move):
                current_move_number = int(move[:-1])
                continue
            # if not, then it's a move
            # if there is a space in the middle, split into white and black moves
            if " " in move:
                # print(move)
                white_move, black_move = move.split()

                # if white move is .. means this is a black variant
                # so let's remove the last move from the list
                if white_move == "..":
                    # if last one was the same number and black, then remove it
                    if self.moves[-1].startswith(f"{current_move_number} black"):
                        self.moves.pop()
                        self.next_one = BLACK
                else:
                    self.update_memory(white_move)
                    white_move = translate_move(
                        white_move, self.current_pause())
                    description = f"{current_move_number} white {white_move}"
                    self.moves.append(description)

                self.update_memory(black_move)
                black_move = translate_move(black_move, self.current_pause())
                description = f"{current_move_number} black {black_move}"
                self.moves.append(description)
                continue
            # single move no color
            self.update_memory(move)
            move = translate_move(move, self.current_pause())
            self.moves.append(f"{current_move_number} white {move}")

    def set_name(self, comment):
        self.name += " " + comment.strip()
