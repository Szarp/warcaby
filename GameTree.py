from numpy import double, mean
from Pawn import Pawn
from Leaf import Leaf
from typing import List
from Board import initialize_board, print_board, game_status
import time
from evaluate import statistics


class GameTree:
    def __init__(
        self,
        begining_layout: List = None,
        alfabeta: bool = False,
        white_depth: int = 2,
        black_depth: int = 2,
        player: str = "white",
        white_eval: list = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2],
        black_eval: list = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2],
    ) -> None:
        if begining_layout != None:
            self.board = begining_layout  # init_board_from_layout(begining_layout)
        else:
            self.board: List[Pawn] = initialize_board()
        self.player: str = player
        self.white_depth: int = white_depth
        self.black_depth: int = black_depth
        self.white_eval: list = white_eval
        self.black_eval: list = black_eval
        self.moves_without_capture: int = 0
        self.alfabeta = alfabeta
        self.root: Leaf = Leaf(
            board=self.board,
            color=self.player,
            moves_without_capture=self.moves_without_capture,
            alfabeta=self.alfabeta,
        )
        self.game_status: str = game_status(self.board, self.player, self.moves_without_capture)
        self.all_moves: list = []
        self.black_move_time: list = []
        self.white_move_time: list = []

    def build_tree_game(self) -> double:
        start = time.time()
        if self.root.color == "white":
            build_tree_game(self.root, self.white_depth)
        else:
            build_tree_game(self.root, self.black_depth)
        end = time.time()
        return end - start

    def choose_ai_move(self):
        elems = [leaf.evaluation for leaf in self.root.leafs]
        return elems.index(self.root.evaluation)

    def choose_move(self, move: int):
        if move in range(len(self.root.avaialbe_moves)):
            temp: Leaf = self.root.leafs.pop(move)
            self.root = temp
            self.root.root = None
            self.board = self.root.board
            t: double = self.build_tree_game()
            self.all_moves.append(move)
            if self.root.color == "white":
                self.white_move_time.append(t)
            else:
                self.black_move_time.append(t)
            self.game_status = self.root.game_status
            self.moves_without_capture = self.root.moves_without_capture
        else:
            print("Wrong move")
        pass

    def show_moves(self):
        available_moves = self.root.avaialbe_moves
        self.game_status = self.root.game_status
        for i, move in enumerate(available_moves):
            # print(
            #     f"{i}. begin:{move[0].position} end:{move[1]} eval:{self.root.leafs[i].evaluation if self.root.leafs != [] else None }"
            # )
            print(f"{i}. begin:{move[0].position} end:{move[1]}")
        pass

    def show(self):
        print_board(self.board)
        print(f"{self.root.color} player move")
        self.show_moves()

    def show_game_status(self):
        if self.game_status:
            return True, [
                self.game_status,
                len(self.all_moves),
                mean(self.black_move_time),
                mean(self.white_move_time),
            ]
        return False, []

    def white_wins(self):
        return self.game_status == "Whites win"


def build_tree_game(root_node: Leaf = None, max_depth: int = 0):
    if root_node.game_status != None:
        wages = root_node.white_eval if root_node.color == "white" else root_node.black_eval
        s: statistics = statistics(root_node.board, root_node.game_status, wages=wages)
        s.iterate_board()
        root_node.evaluation = s.board_evaluation()
        return
    if root_node.count_parents() == max_depth:
        wages = root_node.white_eval if root_node.color == "white" else root_node.black_eval
        s: statistics = statistics(root_node.board, root_node.game_status, wages=wages)
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
                    alfabeta=root_node.alfabeta,
                )
                l.root = root_node
                root_node.leafs.append(l)
                build_tree_game(l, max_depth=max_depth)
                if root_node.alfabeta:
                    e = [leaf.evaluation for leaf in root_node.leafs]
                    root_node.evaluation = max(e) if root_node.color == "white" else min(e)
                    if root_node.root:
                        if root_node.root.evaluation:
                            cut = root_node.root.evaluation > root_node.evaluation
                            if cut and root_node.root.color == "black":
                                break
                            if not cut and root_node.root.color == "white":
                                break
        else:
            for l in root_node.leafs:
                build_tree_game(l, max_depth=max_depth)
        e = [leaf.evaluation for leaf in root_node.leafs]
        root_node.evaluation = max(e) if root_node.color == "white" else min(e)
        if root_node.root:
            root_node.root.evaluation = root_node.evaluation
