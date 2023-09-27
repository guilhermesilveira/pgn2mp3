import re
from moves import long_move_name

branch_counter = 0


WHITE = "white"
BLACK = "black"
SHORT_PAUSE = "<break time=\"0.5s\"/>"
LONG_PAUSE = "<break time=\"2.2s\"/>"


def _clear_comment(comment: str):
    # removes everything between [ and ]
    return re.sub(r"\[.*?\]", "", comment).strip()


class Move:
    def __init__(self, color, san, comment):
        self.color = color
        self.san = san
        self.comment = _clear_comment(comment)

    def to_spoken_str(self, pause_type):
        if self.comment:
            extra = " (" + self.comment + ") "
        else:
            extra = ""
        return long_move_name(self.san) + extra + pause_type

    def to_simple_str(self):
        return self.san

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.color} {self.san} {self.comment}"


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


class Moves:
    def __init__(self, moves: list[Move]):
        self.moves = moves

    def simple_str(self):
        moves_as_str = [str(move.san) for move in self.moves]
        return ",".join(moves_as_str)

    def length(self):
        return len(self.moves)

    def is_fully_memorized(self, memory: Memory):
        current_simple_str = ""
        for i, move in enumerate(self.moves):
            current_simple_str += "," + move.to_simple_str()
            if not memory.is_memorized(current_simple_str):
                return False
        return True

    def to_spoken_str(self, memory: Memory):
        current_pause_type = SHORT_PAUSE
        moves_as_str = []
        current_simple_str = ""
        is_memorized = True
        for move in self.moves:
            current_simple_str += "," + move.to_simple_str()
            if is_memorized and not memory.is_memorized(current_simple_str):
                current_pause_type = LONG_PAUSE
                is_memorized = False
            moves_as_str.append(move.to_spoken_str(current_pause_type))
        return ". ".join(moves_as_str)


class Branch:
    def __init__(self, title,
                 parent=None,
                 memory: Memory = None,
                 moves: list = None):
        global branch_counter
        branch_counter += 1
        self.name = f"{title} branch {branch_counter}"
        self.memory = memory
        self.parent = parent

        # copy moves from parent if parent
        if parent:
            self.moves = parent.moves.copy()
        else:
            self.moves = Moves(moves) if moves is None else Moves(moves)

    def move_count(self):
        # length of moves
        return self.moves.length()

    def get_name(self):
        return self.name
