# tests/test_branch.py

import unittest
from branch import translate_move, PAUSE


class TestTranslateMove(unittest.TestCase):

    def test_translate_move_king(self):
        self.assertEqual(translate_move("Ke4"), f"king e4{PAUSE}")

    def test_translate_move_queen(self):
        self.assertEqual(translate_move("Qxe5+"),
                         f"queen  captures e5 check {PAUSE}")

    def test_translate_move_kingside_castle(self):
        self.assertEqual(translate_move("O-O"), f"kingside castle {PAUSE}")

    def test_translate_move_queenside_castle(self):
        self.assertEqual(translate_move("O-O-O"), f"queenside castle {PAUSE}")

    def test_translate_move_pawn(self):
        self.assertEqual(translate_move("e5"), f"pawn e5{PAUSE}")

    def test_translate_move_pawn_capture(self):
        self.assertEqual(translate_move("exd5"), f"pawn e captures d5{PAUSE}")

    def test_translate_move_extras(self):
        self.assertEqual(translate_move("exd5+"),
                         f"pawn e captures d5 check {PAUSE}")

    # Add more tests as required.


if __name__ == "__main__":
    unittest.main()
