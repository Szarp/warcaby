from data import games
from Pawn import Pawn


def pos_form_black_square(black_square: int):
    y = black_square // 4
    y = y - 1 if black_square % 4 == 0 else y
    x = (black_square - 4 * (y)) * 2
    x = x - 1 if y % 2 == 0 else x
    return [y, x]


def prepare_board(whose_turn, white_man, black_man):
    color = "white" if whose_turn == "W" else "black"
    pawns = []
    black = [Pawn("black", pos_form_black_square(int(square))) for square in black_man.split(",")]
    white = [Pawn("white", pos_form_black_square(int(square))) for square in white_man.split(",")]
    return color, white + black


def get_game(game_num: int):
    g: str = games[game_num]
    whose_turn, white_man, black_man = g.split(":")
    return prepare_board(whose_turn, white_man, black_man)
