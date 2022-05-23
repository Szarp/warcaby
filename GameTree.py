from logging import root

from matplotlib.style import available
from Pawn import Pawn
from Leaf import Leaf
from typing import List
from Board import initialize_board, print_board, game_status
import time
from evaluate import statistics


class GameTree:
    def __init__(
        self, begining_layout: List = None, alfabeta: bool = False, depth: int = 2,
    player:str = "white") -> None:
        if begining_layout != None:
            self.board = begining_layout  # init_board_from_layout(begining_layout)
        else:
            self.board: List[Pawn] = initialize_board()
        self.player: str = player
        self.depth: int = depth
        self.moves_without_capture: int = 0
        self.root: Leaf = Leaf(board=self.board,color=self.player,moves_without_capture=self.moves_without_capture)
        self.game_status: str = game_status(self.board, self.player, self.moves_without_capture)

    def build_tree_game(self):
        start = time.time()
        build_tree_game(self.root, self.depth)
        end = time.time()
        print(f"building model time: {end - start}")
    def choose_ai_move(self):
        elems = [leaf.evaluation for leaf in self.root.leafs]
        return elems.index(self.root.evaluation)
    def choose_move(self, move: int):
        if move in range(len(self.root.avaialbe_moves)):
            temp: Leaf = self.root.leafs.pop(move)
            # del self.root
            self.root = temp
            self.root.root = None
            self.board = self.root.board
            self.build_tree_game()
            # self.game_status = game_status(self.board)
            self.game_status = self.root.game_status
            self.moves_without_capture  = self.root.moves_without_capture
        else:
            print("Wrong move")
        pass

    def show_moves(self):
        available_moves = self.root.avaialbe_moves
        self.game_status = self.root.game_status
        # self.game_status = self.root.game_status
        for i, move in enumerate(available_moves):
            print(f"{i}. begin:{move[0].position} end:{move[1]} eval:{self.root.leafs[i].evaluation if self.root.leafs != [] else None }")
            # [[k[0].position,k[1][0]] for k in self.avaialbe_moves]
        pass

    def show(self):
        print_board(self.board)
        print(f"{self.root.color} player move")
        self.show_moves()

    def show_game_status(self):
        if self.game_status:
            print('Game result: ' + self.game_status)
def build_tree_game(root_node: Leaf = None, max_depth: int = 0):
    # pass
    if root_node.game_status != None:
        s:statistics = statistics(root_node.board,root_node.game_status)
        s.iterate_board()
        root_node.evaluation = s.board_evaluation()
        return
    if root_node.count_parents() == max_depth:
        #TODO propagete evaluation
        #TODO implement alfabeta
        s:statistics = statistics(root_node.board,root_node.game_status)
        s.iterate_board()
        root_node.evaluation = s.board_evaluation()
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
        e = [leaf.evaluation for leaf in root_node.leafs]
        root_node.evaluation = max(e) if root_node.color == "white" else min(e)
