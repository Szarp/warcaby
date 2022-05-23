from Pawn import Pawn
from typing import List
from InitializeBoard import get_color_pawns
from Board import build_board_from_move, get_all_possible_moves, game_status

class Leaf:
    def __init__(
        self,
        board: List[Pawn] = [],
        was_capture_move: bool = False,
        move: list = None,
        moves_without_capture: int = 0,
        color: str = "white",
        white_eval:list = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2],
        black_eval:list = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2]
    ) -> None:
        self.move = move
        self.color = color
        self.board: list = None
        if move != None:
            self.move = move
            self.board = build_board_from_move(board, was_capture_move, self.move)
        else:
            self.board = board
        self.is_capture, self.avaialbe_moves = get_all_possible_moves(self.color, self.board)
        self.moves_without_capture: int = 0 if was_capture_move else moves_without_capture + 1
        self.leafs: List[Leaf] = []
        self.root: Leaf = None
        self.game_status = game_status(self.board,self.color,queen_moves=self.moves_without_capture)
        self.evaluation:int = None
        self.black_eval:list = black_eval
        self.white_eval:list = white_eval

    def count_parents(self, i=0):
        if self.root == None:
            return i
        else:
            return self.root.count_parents(i + 1)

    def other_color(self):
        return "black" if self.color == "white" else "white"

    def __str__(self) -> str:
        ret = "  " * self.count_parents()
        ret += f" └─ {self.color} move"
        ret += f" Eval:{self.evaluation} Move:{self.move[0].position if self.move else self.move} {self.move[1]if self.move else self.move}\n"
        for k in self.leafs:
            ret += k.__str__()
        return ret
