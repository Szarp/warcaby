from asyncio import base_events
import re
from tkinter.messagebox import NO
from typing import List
from Pawn import Pawn
from InitializeBoard import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Board_layout:
    def __init__(self) -> None:
        self.black_fields_array = np.array(
            [
                [0, 0, 0, 5, 1, 0, 0, 0],
                [0, 0, 13, 9, 6, 2, 0, 0],
                [0, 21, 17, 14, 10, 7, 3, 0],
                [29, 25, 22, 18, 15, 11, 8, 4],
                [0, 30, 26, 23, 19, 16, 12, 0],
                [0, 0, 31, 27, 24, 26, 0, 0],
                [0, 0, 0, 32, 28, 0, 0, 0],
            ]
        )


class Board:
    def __init__(
        self,
        white_pos: list = [],
        black_pos: list = [],
        white_king: list = [],
        black_king: list = [],
    ) -> None:
        self.black: list = black_pos
        self.white: list = white_pos
        self.black_king: list = black_king
        self.white_king: list = white_king
        pass


# Hanna mazur i jej mąż co tu robisz? xd
def basic_evaluation(board):
    return (
        len(get_color_pawns("black", board))
        - len(get_color_pawns("white", board))
        # + 5 * (len(board.black_king) - len(board.white_king))
    )
    # return 7


class Leaf:
    def __init__(
        self, board: Board, move: list = None, moves_without_capture: int = 0
    ) -> None:
        if move != None:
            self.move = move
            self.board = board  # buid_board_from_move(board_move)
        else:
            self.board = board
        self.is_capture, self.avaialbe_moves = False, [
            1,
            2,
            3,
        ]  # build_moves_from_board(board,player)
        # self.is_capture,self.avaialbe_moves = build_moves_from_board(board,player)
        self.evaluation: int = basic_evaluation(self.board)
        self.moves_without_capture: int = moves_without_capture
        self.leafs: list(Leaf) = []
        self.root: Leaf = None

    def __str__(self) -> str:
        ret = ""
        for k in self.leafs:
            ret += "  " * self.count_parents() 
            temp = k.__str__()
            ret += " └─ Next\n"if temp != "" else " ├─ Next\n"
            ret += temp
        return ret
        # return f'Node'

    def count_parents(self,i=0):
        # i = 0
        if self.root == None:
            return i
        else:
            return self.root.count_parents(i+1)
        # while r != None:
        #     i += 1
        #     r = self.root.root
        #     print(r,type(r))
        # return i


class GameTree:
    def __init__(
        self, begining_layout: list = None, alfabeta: bool = False, depth: int = 4
    ) -> None:
        if begining_layout != None:
            self.board = ""  # init_board_from_layout(begining_layout)
        else:
            self.board: list = initialize_board()
        self.player: str = "white"
        self.depth: int = depth
        self.moves_without_capture: int = 0
        self.root: Leaf = Leaf(board=self.board)
        # for k in range(3):
        #     l:Leaf = Leaf(
        #         board = self.root.board,
        #         move=k,
        #         moves_without_capture=self.root.moves_without_capture
        #     )
        #     l.root = self.root
        #     self.root.leafs.append(l)

    def build_tree_game(self):
        build_tree_game(self.root, 0, self.depth)
        # for _ in range(self.depth):
        #     for one_leaf in self.root.leafs:
        #         for k in range(3):
        #             one_leaf.leafs.append(
        #                 Leaf(
        #                     board = self.root.board,
        #                     move=k,
        #                     moves_without_capture=one_leaf.moves_without_capture+1,
        #                 )
        #             )
        # one_leaf.leafs = build_available_moves(one_leaf)


def build_tree_game(root_node: Leaf = None, actual_depth: int = 0, max_depth: int = 0):
    # pass
    if root_node.count_parents() == max_depth:
        return
    else:
        # for one_leaf in root.leafs:
        if len(root_node.leafs) == 0:
            for k in range(3):
                l: Leaf = Leaf(
                    board=root_node.board,
                    move=k,
                    moves_without_capture=root_node.moves_without_capture + 1,
                )
                l.root = root_node
                root_node.leafs.append(l)
                build_tree_game(l, actual_depth + 1, max_depth=max_depth)
        # return
        # one_leaf.leafs = build_available_moves(one_leaf


if __name__ == "__main__":
    print("Hello world!")
    # print(f"\u26c0 \u26c1 \u26c2 \u26c3")

    # pawns = initialize_board()
    g: GameTree = GameTree()
    g.build_tree_game()
    print(g.root)
    pass
    # print_board(pawns)
    # for x in pawns:
    #     x.print()
