from asyncio import base_events
from logging import root
from operator import is_
import re
from tkinter import E
from tkinter.messagebox import NO
from typing import List
from Pawn import Pawn
from Board import *
from GameTree import GameTree
from game_parser import get_game
from elo import Elo
import random
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
    t = game.build_tree_game()
    while True:
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
            start_game()
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
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
    startup_menu()