from asyncio import base_events
from logging import root
from operator import is_
import re
from tkinter import E
from tkinter.messagebox import NO
from typing import List
from Pawn import Pawn
from Leaf import Leaf
from Board import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GameTree import GameTree
from game_parser import get_game
from elo import Elo
import random

# import keyboard
from time import sleep
import os
import threading

g: GameTree = None
league:Elo = Elo(k=20)
league.create_players()
sim2 = simulation(
    [
        Pawn("black", [5, 2]),
        Pawn("white", [6, 3]),
        Pawn("black", [5, 4]),
        Pawn("black", [3, 2]),
        Pawn("black", [3, 4]),
    ]
)
sim7 = simulation([Pawn("black", [6, 7]), Pawn("white", [7, 6])])
queen = Pawn("white", [5, 2])
queen.is_queen = True


def clearConsole():
    cmd = "cls"
    os.system(cmd)
def execute_game(name1:str="",name2:str="",layout:int=-1):
    global league
    board = []
    p1:list = []
    p2:list = []
    if layout > 0:
        layout_num = layout
    else:
        layout_num =random.randint(0,887)
    player,board = get_game(layout_num)
    if name1 == "":
        name1,[_,white_depth,white_eval] = league.get_random_player()
    else:
        name1,[_,white_depth,white_eval] = league.get_random_player(name1)
    if name2 == "":   
        name2,[_,black_depth,black_eval] = league.get_random_player()
    else:
        name2,[_,black_depth,black_eval] = league.get_random_player(name2)
    game = GameTree(
        begining_layout=board,
        player=player,
        white_depth=white_depth,
        black_depth=black_depth,
        white_eval=white_eval,
        black_eval=black_eval,
    )
    # print("White",name1,white_depth,white_eval)
    # print("Black",name2,black_depth,black_eval)
    # print("Game",layout_num)
    # white_player black_player game build_time, winner, all_moves,avg_white_move, avg_black_move
    t = game.build_tree_game()
    # print(f'Begin time: {t}')
    while True:
            # clearConsole()
            # g.show()
        end,status = game.show_game_status()
        if end:
            if game.white_wins:
                league.gameOver(name1,name2)
            else:
                league.gameOver(name1,name2)
            break
        i = game.choose_ai_move()
        game.choose_move(i)
    print(f"{name1};{name2};{layout_num};{t};{status[0]};{status[1]};{status[2]};{status[3]}")
            # clearConsole()
    # black = league.get_random_player()
def play_many_games(num:int=100,max_threds=2):
    tasks = [multi_game for _ in range(max_threds)]
    for t in tasks:
        t = threading.Thread(target=t)
        t.start()
def multi_game(num:int=1):
    for _ in range(num):
        execute_game()
def start_game(beginning_layout=None, player="white",white_depth:int=2,black_depth:int=2,alfabeta:bool=True):
    global g
    white_eval = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2]
    black_eval = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2]
    white_depth =white_depth
    black_depth = black_depth
    g = GameTree(
        begining_layout=beginning_layout,
        player=player,
        white_depth=white_depth,
        black_depth=black_depth,
        white_eval=white_eval,
        black_eval=black_eval,
        alfabeta=alfabeta
    )
    return g.build_tree_game()

def startup_menu():
    global g
    choice = 0
    while choice != 5:
        print("Wybierz, co chcesz wyświetlić:")
        print("1 - Man vs Man")
        print("2 - Man vs AI") 
        print("3 - AI vs AI") 
        print("4 - Tournament")
        print("5 - Wyjdz z menu")
        try:
            choice = int(input())
        except:
            print("Prosze podaj numer wyboru")
        if choice < 1 or choice > 4:
            print("Podano złą wartość, spróbuj ponownie")
        if choice == 1:
            # start_game(sim7 + [queen])
            color, game = get_game(0)
            start_game(game,player=color,alfabeta=False)
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
                    print(f'Game result: {stats[0]} Game moves: {stats[1]} Avarege black time:{stats[2]} Avarege white time{stats[3]}')
                    break
                print(f"Choose move: {0}-{len(g.root.avaialbe_moves)-1}")
                inp = input()
                if inp.isdigit():
                    stand = int(inp)
                else:
                    stand = -1
                if stand >= 0 :
                    if stand < len(g.root.avaialbe_moves):
                        g.choose_move(stand)
                    pass
                if stand == 100:
                    break
                clearConsole()
            break
        elif choice == 2:
            print(f"Man's color; w - white b - black")
            color = "white" if str(input()) == "w" else "black"
            print(f"Choosed {color}")
            #  game = get_game(0)
            # game = initialize_board()
            start_game()
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
                    # print("Game result: " + self.game_status)
                    # print(f'Game moves: {len(self.all_moves)}')
                    # print(f'Avarege black time: {mean(self.black_move_time)}')
                    # print(f'Avarege white time: {mean(self.white_move_time)}')
                    print(f'Game result: {stats[0]} Game moves: {stats[1]} Avarege black time:{stats[2]} Avarege white time{stats[3]}')
                    break
                if g.root.color == color:
                    print(f"Choose move: {0}-{len(g.root.avaialbe_moves)-1}")
                    stand = int(input())
                    if stand >= 0 and stand < len(g.root.avaialbe_moves):
                        g.choose_move(stand)
                        pass

                    if stand == 100:
                        break
                else:
                    i = g.choose_ai_move()
                    g.choose_move(i)
                clearConsole()
            break
        elif choice == 3:
            # start_game(sim7+[queen])
            start_game()
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
                    print(f'Game result: {stats[0]} Game moves: {stats[1]} Avarege black time:{stats[2]} Avarege white time{stats[3]}')
                    break
                i = g.choose_ai_move()
                g.choose_move(i)
                clearConsole()
            break
        elif choice == 4:
            clearConsole()
            play_many_games()
            # execute_game()
        else:
            pass

if __name__ == "__main__":
    print("Hello world!")
    # play_many_games()
    # while True:
    #     alive = [t.is_alive() for t in threading.enumerate()]
    #     if not any(alive[1:]):
    #         for k,value in league.ratingDict.items():
    #             print(f'{k};{value[0]}')

    #             # print(league.get_best_players())
    #         break
    #     sleep(10)
    # execute_game("Alexandra Thornton","Barclay Walsh",546)
    # start_game(sim7 + [queen])
    startup_menu()
    # color, game = get_game(0)
    # t = start_game(game,player=color)
    # # print(g.root)
    # print(t,g.root.count_leafs())
    sim3 = simulation(
        [
            Pawn("black", [5, 2]),
            Pawn("black", [5, 6]),
            Pawn("black", [5, 4]),
            Pawn("black", [3, 2]),
            Pawn("black", [3, 4]),
        ]
    )
    sim4 = simulation([Pawn("black", [4, 5]), Pawn("black", [1, 2]), Pawn("black", [5, 6])])
    sim5 = simulation([Pawn("black", [4, 3]), Pawn("black", [3, 6]), Pawn("black", [1, 4])])
    sim6 = simulation(
        [
            Pawn("black", [4, 1]),
            Pawn("black", [2, 3]),
            Pawn("black", [4, 5]),
            Pawn("white", [5, 0]),
            Pawn("white", [5, 6]),
        ]
    )
    # get_available_captures(sim,sim[0])
    # print_board(sim5 + [queen])
    # temp = [[2, 5], [4, 7]]
    # temp.extend([[2, 5], [0, 3]])
    # print(temp)
    # _, c = get_available_captures(sim4,queen)
    # print(c)
    # print(get_all_possible_moves("white", sim5 + [queen]))
    # print(get_pawn_between(sim6, [7,2], [2,7]).print())
    # print(sim4+[queen])
    # print(get_pawn_moves(sim4, sim4[0]))
    # c = get_captures(sim5, queen)
    # print("c", c)
    # for k in range(len(b)):
    #     print("b",b[k])
    # pass
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
    # flatten - done
    # is_capture_move, moves = get_all_possible_moves (color) -> zwraca tylko bicia albo tylko ruchy - done
    # board = create_new_board_from_move(board,move)
    # evaluate(board) ->  I choose move nr 3 ([0,2])
    # promotion (pawn) - done
    # game_status(board) ->win/lose/draw - done
    # evaluate(board) - done
    # perform_capture_move - done
    # perform_positional_move -done


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
