from ast import operator
from turtle import position

from pyparsing import col
from Board import *

from Pawn import Pawn


class statistics:
    def __init__(self, board, game_status, wages=[1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2]) -> None:
        self.board = board
        self.pawns = 0  # ok 0.
        self.queens = 0  # ok 1.
        self.safe_pieces = 0  # ok 2.
        self.distance_to_promotion = 0  # ok 3.
        self.free_space_on_promotion = 0  # ok 4.
        self.defender_pieces = 0  # ok 5.
        self.attacking_pieces = 0  # ok 6.
        self.central_pieces = 0  # ok 7.
        self.main_diagonal_pieces = 0  # ok 8.
        self.double_diagonal_pieces = 0  # ok 9.
        self.wages = wages
        self.game_status = game_status

    def iterate_board(self):
        p: Pawn = None
        for p in self.board:
            x, y = p.position
            color = p.color
            operation = 1 if color == "white" else -1
            if p.is_queen:
                self.queens += 1 * operation
            else:
                if color == "black":
                    self.distance_to_promotion += x * operation
                else:
                    self.distance_to_promotion += (7 - x) * operation
                self.pawns += 1 * operation
            if 0 in p.position or 1 in p.position:
                self.safe_pieces += 1 * operation
            if abs(x - y) == 1:
                self.double_diagonal_pieces += 1 * operation
            if x + y == 7:
                self.main_diagonal_pieces += 1 * operation
            if y < 2:
                if color == "black":
                    self.defender_pieces += 1 * operation
                else:
                    self.attacking_pieces += 1 * operation
            if y > 5:
                if color == "white":
                    self.defender_pieces += 1 * operation
                else:
                    self.attacking_pieces += 1 * operation
            if x in range(2, 5) and y in range(2, 5):
                self.central_pieces += 1 * operation
            if x == 0:
                self.free_space_on_promotion -= 1
            if x == 7:
                self.free_space_on_promotion += 1

    def board_evaluation(self):
        if self.game_status == 'Whites win':
            return 100
        elif self.game_status == 'Blacks win':
            return -100
        elif self.game_status == 'Draw':
            return 0
        else:
            return (
                self.pawns * self.wages[0]
                + self.queens * self.wages[1]  # ok 1.
                + self.safe_pieces * self.wages[2]  # ok 2.
                + self.distance_to_promotion * self.wages[3]  # ok 3.
                + self.free_space_on_promotion * self.wages[4]  # ok 4.
                + self.defender_pieces * self.wages[5]  # ok 5.
                + self.attacking_pieces * self.wages[6]  # ok 6.
                + self.central_pieces * self.wages[7]  # ok 7.
                + self.main_diagonal_pieces * self.wages[8]  # ok 8.
                + self.double_diagonal_pieces * self.wages[9]  # ok 9.
            )


# 1. Number of pawns;
# def pawns(self):
#     pass
# 2. Number of queens;
# def queens(self):
#     pass
# 3. Number of safe pawns (i.e. adjacent to the edge of the board);
# def safe_pawns(self):
#     pass
# 4. Number of safe kings;
# def safe_queen(self):
#     pass
# 5. Number of moveable pawns (i.e. able to perform a move other than capturing).
# def count_pawns_moves(self):
#     pass
# 6. Number of moveable kings. Parameters 5 and 6 are calculated taking no notice of capturing priority;
# def count_queens_moves(self):
#     pass
# 7. Aggregated distance of the pawns to promotion line;
# def distance_to_promotion(self):
# sum(piece.height) - sum(BOARD_HEIGHT-piece.height)
# pass
# 8. Number of unoccupied fields on promotion line.
# def free_space_on_promotion(self):
#     #0-BOARD_WIDTH/2
#     pass
# Heuristics could also consider sums of or differences in respective parameters for both
# players rather than raw numbers for each player separately. Once heuristics using the
# straightforward parameters listed above had been generated and tested, it was decided
# that it would be desirable to add more sophisticated parameters characterizing layout of
# the pieces on the board. The following parameters were, therefore, introduced:
# 9. Number of defender pieces2 (i.e. the ones situated in two lowermost rows);
# def defender_pieces(self):
#     pass
# 10. Number of attacking pawns (i.e. positioned in three topmost rows);
# def attacking_pieces(self):
#     pass
# 11. Number of centrally positioned pawns (i.e. situated on the eight central squares of the board);
# def central_pawns(self):
#     pass
# 12. Number of centrally positioned kings;
# def central_queens(self):
#     pass
# 13. Number of pawns positioned on the main diagonal;
# def main_diagonal_pawns(self):
#     # x == (BOARD_HEIGHT-y)
#     pass
# 14. Number of kings positioned on the main diagonal;
# def main_diagonal_queens(self):
#     pass
# 15. Number of pawns situated on double diagonal;
# def double_diagonal_pawns(self):
#     pass
# 16. Number of kings situated on double diagonal;
# def double_diagonal_queens(self):
#     pass
# 17. Number of loner pawns. Loner piece is defined as the one not adjacent to any other
# def loner_pawns(self):
#     pass
# 18. Number of loner kings;
# def loner_kings(self):
#     pass
# 19. Number of holes, i.e. empty squares adjacent to at least three pieces of the same color.
# Apart from the above parameters six patterns were defined. They are described below
# using common notation presented in Fig. 2. Since only one instance of each pattern can
# exist for any of the players at the same time, features 20− 25 can take only boolean values.
# 20. Presence of a Triangle pattern(see Fig. 3(a)).
# 21. Presence of an Oreo pattern (see Fig. 3(b)).
# 22. Presence of a Bridge pattern (see Fig. 3(c)).
# 23. Presence of a Dog pattern (see Fig. 3(d)).
# 24. Presence of a pawn in corner (i.e. White (Black) pawn on square 29 (4), resp.);
# 25. Presence of a king in corner (i.e. White (Black) king on square 4 (29), resp.);
# https://pages.mini.pw.edu.pl/~mandziukj/PRACE/es_init.pdf

# def evaluate(board,param_list:list[]):
#     return p1*param_list[0] + ... +
