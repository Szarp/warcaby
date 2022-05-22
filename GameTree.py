from logging import root

from matplotlib.style import available
from Pawn import Pawn
from Leaf import Leaf
from typing import List
from Board import initialize_board, print_board
import time


class GameTree:
    def __init__(
        self, begining_layout: List = None, alfabeta: bool = False, depth: int = 2
    ) -> None:
        if begining_layout != None:
            self.board = ""  # init_board_from_layout(begining_layout)
        else:
            self.board: List[Pawn] = initialize_board()
        self.player: str = "white"
        self.depth: int = depth
        self.moves_without_capture: int = 0
        self.root: Leaf = Leaf(board=self.board)

    def build_tree_game(self):
        start = time.time()
        build_tree_game(self.root, self.depth)
        end = time.time()
        print(f"building model time: {end - start}")

    def choose_move(self, move: int):
        if move in range(len(self.root.avaialbe_moves)):
            temp: Leaf = self.root.leafs.pop(move)
            # del self.root
            self.root = temp
            self.root.root = None
            self.board = self.root.board
            self.build_tree_game()
            pass
        else:
            print("Wrong move")
        pass

    def show_moves(self):
        available_moves = self.root.avaialbe_moves
        for i, move in enumerate(available_moves):
            print(f"{i}. begin:{move[0].position} end:{move[1]}")
            # [[k[0].position,k[1][0]] for k in self.avaialbe_moves]
        pass

    def show(self):
        print_board(self.board)
        print(f"{self.root.color} player move")
        self.show_moves()


def build_tree_game(root_node: Leaf = None, max_depth: int = 0):
    # pass
    if root_node.count_parents() == max_depth:
        # wykonujemy evaluacje
        # tutaj nastąpi propagacja wartości do rodzica
        return
    else:
        if len(root_node.leafs) == 0:
            for k in root_node.avaialbe_moves:
                l: Leaf = Leaf(
                    board=root_node.board,
                    was_capture_move=root_node.is_capture,
                    move=k,
                    moves_without_capture=root_node.moves_without_capture,
                    color=root_node.other_color(),
                )
                l.root = root_node
                root_node.leafs.append(l)
                build_tree_game(l, max_depth=max_depth)
        else:
            for l in root_node.leafs:
                build_tree_game(l, max_depth=max_depth)
