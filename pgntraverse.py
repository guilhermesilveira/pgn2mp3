from google.oauth2 import service_account
from google.cloud import texttospeech
from tqdm import tqdm
import os
import logging
from cache import Cache
from tts import GoogleVoicer
from branch import Branch, LONG_PAUSE, reset_branch_counter, Memory, Move
import hashlib
from pgn_parser import pgn, parser


def traverse_branch(title: str, current_status, move_list: list, voicer, memory: Memory = None):

    total_moves = len(current_status)

    for i_move, movetext in enumerate(current_status):
        white = movetext.white
        black = movetext.black
        # print(move_list, movetext)

        # white variations
        for variation in white.variations:
            # print(variation)
            traverse_branch(title, variation, move_list.copy(), voicer, memory)

        if white.san != '':
            move_list.append(Move("white", white.san, white.comment))
            # print(f"'{white.san}'")

        # black variations
        for variation in black.variations:
            # print(variation)
            traverse_branch(title, variation, move_list.copy(), voicer, memory)

        if black.san != '':
            move_list.append(Move("black", black.san, black.comment))
            # print(f"'{black.san}'")

        if i_move == total_moves - 1:
            printer.save(Branch(title,
                                parent=None,
                                memory=memory,
                                moves=move_list),
                         voicer,
                         memory)


class Printer:
    printed = set()
    memorized_count = 0
    cached_count = 0
    print_count = 0
    reprint_count = 0

    def __str__(self):
        return f"Printer: Cached: {self.cached_count} Memorized: {self.memorized_count} Reprint: {self.reprint_count} Printed: {self.print_count}"

    def __repr__(self):
        return self.__str__()

    def save(self, branch: Branch, voicer, memory):
        moves = branch.moves

        if moves.is_fully_memorized(memory):
            self.memorized_count += 1
            print(f"Skipping: {branch.get_name()} fully memorized")
            return

        # generates a md5 from the moves array
        # if it's already been printed, skip it
        # if it hasn't, print it and add it to the printed set
        moves_str = moves.simple_str()
        md5 = hashlib.md5(moves_str.encode('utf-8')).hexdigest()
        if md5 in self.printed:
            self.reprint_count += 1
            print(f"Skipping: {branch.get_name()} reprint within same run")
            return

        spoken_text = branch.get_name() + LONG_PAUSE + moves.to_spoken_str(memory) + '.'
        print(f"Printing: {branch.get_name()} {branch.move_count()} moves")
        if voicer.speak(branch.get_name(), spoken_text):
            self.print_count += 1
        else:
            self.cached_count += 1
        self.printed.add(md5)


printer = Printer()


def _process_file(filename: str,
                  parser,
                  base_path: str):
    with open(filename, 'r') as f_in:
        contents = f_in.read()
        events = contents.split('\n\n\n')
        for event in events:
            if event.startswith('[Event "'):
                name = event.split('"')[1]
                # include '1. ' in the second element
                moves_list = event.split('1. ', 1)
                moves = '1. ' + moves_list[1] if len(moves_list) > 1 else ''
                parser.parse(moves, name, base_path)


class ChessParser:

    def __init__(self, memory: Memory):
        self.memory = memory

    def parse_file(self,
                   filename: str,
                   base_path: str):
        _process_file(filename, self, base_path)

    def parse(self,
              pgn_string: str,
              core_key, base_path=""):

        reset_branch_counter()

        actions = pgn.Actions()
        # replace ?? from pgn_string to nothing
        pgn_string = pgn_string.replace("??", "")

        # replace using regex "{[%eval digits.digits]}" to nothing
        import re
        pgn_string = re.sub(r"\{\s*(\[%eval \d+.\d+\]\s*\})", "", pgn_string)

        game = parser.parse(pgn_string, actions=actions)

        voicer = GoogleVoicer(core_key, base_path)
        # TODO 3 of those arguments thosuld be in one object, a printer object or branch creator etc=
        # perhpas move the function here
        traverse_branch(core_key, game.movetext, [],
                        voicer, self.memory)
