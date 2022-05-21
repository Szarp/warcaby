from asyncio import base_events
import re
from tkinter.messagebox import NO
from typing import List
from Pawn import Pawn
from Leaf import Leaf
from Board import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GameTree import GameTree

if __name__ == "__main__":
    print("Hello world!")
    # print(f"\u26c0 \u26c1 \u26c2 \u26c3")
    # sim = simulation([Pawn('white', [6,1]), Pawn('black', [5,2]), Pawn('black', [3,4])])
    # # print_board(sim)
    # # get_available_captures(sim,sim[0])
    # a = get_captures(sim,sim[0])
    # print("a",a)
    # sim1 = simulation([Pawn('white', [6,1]), Pawn('black', [5,2]), Pawn('black', [3,4]), Pawn('black', [1,6]), Pawn('black', [1,4]), Pawn('black', [1,2])])
    # print_board(sim1)
    # # get_available_captures(sim,sim[0])
    # b = get_captures(sim1,sim1[0])
    # for k in range(len(b)):
    #     print("b",b[k])
    # pass
    # print("b",b[0])
    sim2 = simulation(
        [Pawn("black", [5, 2]), Pawn("black", [5, 4]), Pawn("black", [3, 2]), Pawn("black", [3, 4])]
    )
    sim3 = simulation(
        [Pawn("black", [5, 2]),Pawn("black", [5, 6]), Pawn("black", [5, 4]), Pawn("black", [3, 2]), Pawn("black", [3, 4])]
    )
    sim4 = simulation(
        [Pawn("black", [4, 3]), Pawn("black", [1, 2]), Pawn("black", [5, 6])]
    )
    sim5 = simulation(
        [Pawn("black", [4, 3]), Pawn("black", [3, 6]), Pawn("black", [1, 4])]
    )
        # get_available_captures(sim,sim[0])
    queen = Pawn("white", [6, 1])
    queen.is_queen = True
    print_board(sim5+[queen])
    # _, c = get_available_captures(sim4,queen)
    # print(c)
    c = get_captures(sim5, queen)
    # for k in range(len(b)):
    #     print("b",b[k])
    # pass
    print("c", c)
    # pawns = initialize_board()
    # g: GameTree = GameTree(depth=6)
    # print(6)
    # g.build_tree_game()
    # g.depth = 7
    # print(7)
    # g.build_tree_game()
    # g.choose_move(1)
    # # g.depth = 8
    # print("new build with only last depth")
    # g.build_tree_game()
    # # print(g.root)
    # # g.choose_move(1)
    # # print(g.root)
    # # g.choose_move(1)
    # # print(g.root)
    # # g.build_tree_game()
    # pass

    # print_board(pawns)
    # for x in pawns:
    #     x.print()


    ## interfeejs 
    #flatten
    # is_capture_move, moves = get_all_possible_moves (color) -> zwraca tylko bicia albo tylko ruchy
    # board = create_new_board_from_move(board,move)
    # evaluate(board) ->  I choose move nr 3 ([0,2])
    # promotion (pawn)
    # game_status(board) ->win/lose/draw
    # evaluate(board) 
    # perform_capture_move
    # perform_positional_move
    

	# def move_limit_reached(self):
	# 	return self.moves_since_last_capture >= self.consecutive_noncapture_move_limit

	# def is_over(self):
	# 	return self.move_limit_reached() or not self.get_possible_moves()

	# def get_winner(self):
	# 	if self.whose_turn() == 1 and not self.board.count_movable_player_pieces(1):
	# 		return 2
	# 	elif self.whose_turn() == 2 and not self.board.count_movable_player_pieces(2):
	# 		return 1
	# 	else:
	# 		return None


    # my_rating = 0
    #     opponents_rating = 0
    #     size=len(self.board)
    #     for i in range(size):
    #         for j in range((i + 1) % 2, size, 2):
    #             piece = self.board[i][j]
    #             if (piece != 0): # field is not empty
    #                 zone=self.check_zone(size, (piece.col, piece.row))
    #                 if piece.color == WHITE: # this is my piece
    #                     if piece.queen:
    #                         my_rating += zone * 5 # this is my queen
    #                     else:
    #                         my_rating += zone * 1 # this is my man
    #                 else:
    #                     if piece.queen:
    #                         opponents_rating += zone * 5 # this is opponent's queen
    #                     else:
    #                         opponents_rating += zone * 1  
    #     # print("Type your message here, you will see it in the log window\n");
    #     return opponents_rating - my_rating
    
    # def check_zone(self, size, field):
    #     y, x = field
    #     zone = 1
        
    #     if y > 0 and x > 0 and y < size - 1 and x < size - 1:
    #         zone = 2
        
    #     if y > 1 and x > 1 and y < size - 2 and x < size - 2:
    #         zone = 3
        
    #     return zone
