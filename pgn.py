from google.oauth2 import service_account
from google.cloud import texttospeech
from tqdm import tqdm
import os
import logging
from cache import Cache
from tts import GoogleVoicer
from branch import Branch, LONG_PAUSE, reset_branch_counter, Memory
import hashlib


class Printer:
    printed = set()

    def save(self, branch: Branch, voicer):
        moves = branch.moves

        # generates a md5 from the moves array
        # if it's already been printed, skip it
        # if it hasn't, print it and add it to the printed set
        md5 = hashlib.md5(','.join(moves).encode('utf-8')).hexdigest()
        if md5 in self.printed:
            print("Skipping: " + branch.get_name())
            return

        spoken_text = branch.get_name() + LONG_PAUSE + '. '.join(moves) + '.'
        print(f"Printing: {branch.get_name()} {branch.move_count()} moves")
        voicer.speak(branch.get_name(), spoken_text)
        self.printed.add(md5)


printer = Printer()


def _process_file(filename: str,
                  parser,
                  memory: Memory,
                  base_path: str):
    with open(filename, 'r') as f_in:
        contents = f_in.read()
        events = contents.split('\n\n')
        for event in events:
            if event.startswith('[Event "'):
                name = event.split('"')[1]
                moves = event.split('1. ')[1]
                print("-----------------------")
                print(name)
                print(moves)
                print()
                parser.parse(memory, name, moves, base_path)


class ChessParser:

    def parse_file(self, filename, memory: Memory,
                   base_path: str):
        _process_file(filename, self, memory, base_path)

    def parse(self, memory, s, core_key, base_path=""):
        voicer = GoogleVoicer(core_key, base_path)

        pos = 0
        reset_branch_counter()
        branches = [Branch(core_key, memory=memory)]
        current_branch = branches[0]

        while pos < len(s):
            if s[pos] == '{':
                pos_end = s.find('}', pos) + 1
                name = s[pos + 1:pos_end - 1]
                # remove any comments from within it
                # comments are contained within []
                while name.find('[') != -1:
                    start = name.find('[')
                    end = name.find(']')
                    name = name[:start] + name[end + 1:]
                # strips it
                name = name.strip()
                # if any name is left
                if name:
                    current_branch.set_name(name)
                pos = pos_end

            elif s[pos] == '(':
                new_branch = Branch(core_key,
                                    parent=current_branch,
                                    memory=memory)
                branches.append(new_branch)
                current_branch = new_branch
                pos += 1

            elif s[pos] == ')':
                printer.save(current_branch, voicer)
                current_branch = current_branch.parent
                branches.pop()
                pos += 1

            elif s[pos] == '*':
                while branches:
                    printer.save(branches.pop(), voicer)
                current_branch = None
                pos += 1

            else:
                move_start = pos
                while pos < len(s) and s[pos] not in ['{', '(', ')', '*', '\n']:
                    pos += 1
                current_move_to_capture = s[move_start:pos]
                current_branch.add_moves(current_move_to_capture)
