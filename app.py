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
    print_board(sim2)
    # get_available_captures(sim,sim[0])
    c = get_captures(sim2, Pawn("white", [6, 3]))
    # for k in range(len(b)):
    #     print("b",b[k])
    # pass
    print("c", c[0])
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
