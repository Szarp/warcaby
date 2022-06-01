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

import random
import os
import threading

g: GameTree = None

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

def start_game(beginning_layout=None, player="white",white_depth:int=6,black_depth:int=6,alfabeta:bool=True):
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
        print("5 - Wyjdz z menu")
        try:
            choice = int(input())
        except:
            print("Prosze podaj numer wyboru")
        if choice < 1 or choice > 4:
            print("Podano złą wartość, spróbuj ponownie")
        if choice == 1:
            start_game(alfabeta=False)
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
            start_game(alfabeta=False)
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
                    print(f'Game result: {stats[0]} Game moves: {stats[1]} Avarege black time:{stats[2]} Avarege white time{stats[3]}')
                    break
                if g.root.color == color:
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
                else:
                    i = g.choose_ai_move()
                    g.choose_move(i)
                clearConsole()
            break
        elif choice == 3:
            # start_game(sim7+[queen])
            start_game(black_depth=6, white_depth=6, alfabeta=True)
            while True:
                clearConsole()
                g.show()
                is_end,stats = g.show_game_status()
                if is_end:
                    print(f'Game result: {stats[0]} Game moves: {stats[1]} Average black time:{stats[2]} Average white time{stats[3]}')
                    break
                i = g.choose_ai_move()
                g.choose_move(i)
                clearConsole()
            break
        else:
            pass

if __name__ == "__main__":
    print("Hello world!")

    startup_menu()