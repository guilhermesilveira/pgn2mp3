from google.oauth2 import service_account
from google.cloud import texttospeech
from tqdm import tqdm
import os
import logging
from cache import Cache
from tts import GoogleVoicer
from branch import Branch, printBranch


class ChessParser:

    def parse(self, memory, s, core_key, base_path=""):
        voicer = GoogleVoicer(core_key, base_path)

        pos = 0
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
                printBranch(current_branch, voicer)
                current_branch = current_branch.parent
                branches.pop()
                pos += 1

            elif s[pos] == '*':
                while branches:
                    printBranch(branches.pop(), voicer)
                current_branch = None
                pos += 1

            else:
                move_start = pos
                while pos < len(s) and s[pos] not in ['{', '(', ')', '*', '\n']:
                    pos += 1
                current_branch.add_moves(s[move_start:pos])
