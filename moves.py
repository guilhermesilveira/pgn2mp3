
# sequence is important
_translation_keys = [
    "K",
    "Q",
    "R",
    "B",
    "N",
    "O-O-O",
    "O-O",
]


translation = {
    "K": "king",
    "Q": "queen",
    "R": "rook",
    "B": "bishop",
    "N": "knight",
    "O-O": "kingside castle",
    "O-O-O": "queenside castle",
}

extras = {
    "+": " check",
    "x": " captures",
    "#": " mate"
}


def long_move_name(move):

    found = False
    # if any of the keys is found, replace it
    for symbol in _translation_keys:
        if symbol in move:
            name = translation[symbol]
            move = move.replace(symbol, f"{name} ")
            found = True
            break
    # if no piece symbol is found, then it's a pawn move
    if not found:
        move = "pawn " + move

    for symbol, name in extras.items():
        if symbol in move:
            move = move.replace(symbol, f"{name} ")
    return move


def translate_move(move, pause):
    move = long_move_name(move)
    return move + pause
