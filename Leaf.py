from Pawn import Pawn
from typing import List
from InitializeBoard import get_color_pawns


def basic_evaluation(board):
    return (
        len(get_color_pawns("black", board))
        - len(get_color_pawns("white", board))
        # + 5 * (len(board.black_king) - len(board.white_king))
    )


class Leaf:
    def __init__(
        self, board: List[Pawn] = [], move: list = None, moves_without_capture: int = 0
    ) -> None:
        self.move = move
        if move != None:
            self.move = move
            self.board = board  # buid_board_from_move(board_move)
        else:
            self.board = board
        self.is_capture, self.avaialbe_moves = False, [1, 2, 3]
        # build_moves_from_board(board,player)
        # self.is_capture,self.avaialbe_moves = build_moves_from_board(board,player)
        self.evaluation: int = basic_evaluation(self.board)
        self.moves_without_capture: int = moves_without_capture
        self.leafs: List[Leaf] = []
        self.root: Leaf = None

    def count_parents(self, i=0):
        if self.root == None:
            return i
        else:
            return self.root.count_parents(i + 1)

    def __str__(self) -> str:
        ret = "  " * self.count_parents()
        ret += " └─ Next"
        ret += f" Eval:{self.evaluation} Move:{self.move}\n"
        for k in self.leafs:
            ret += k.__str__()
        return ret
        # return f'Node'
