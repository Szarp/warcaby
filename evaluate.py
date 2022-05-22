# 1. Number of pawns;
def pawns(board:list):
    pass
# 2. Number of queens;
def queens(board:list):
    pass
# 3. Number of safe pawns (i.e. adjacent to the edge of the board);
def safe_pawns(board:list):
    pass
# 4. Number of safe kings;
def safe_queen(board:list):
    pass
# 5. Number of moveable pawns (i.e. able to perform a move other than capturing).
def count_pawns_moves(board:list):
    pass
# 6. Number of moveable kings. Parameters 5 and 6 are calculated taking no notice of capturing priority;
def count_queens_moves(board:list):
    pass
# 7. Aggregated distance of the pawns to promotion line;
def distance_to_promotion(board:list):
    # sum(piece.height) - sum(BOARD_HEIGHT-piece.height)
    pass
# 8. Number of unoccupied fields on promotion line.
def free_space_on_promotion(board:list):
    #0-BOARD_WIDTH/2
    pass
# Heuristics could also consider sums of or differences in respective parameters for both
# players rather than raw numbers for each player separately. Once heuristics using the
# straightforward parameters listed above had been generated and tested, it was decided
# that it would be desirable to add more sophisticated parameters characterizing layout of
# the pieces on the board. The following parameters were, therefore, introduced:
# 9. Number of defender pieces2 (i.e. the ones situated in two lowermost rows);
def defender_pieces(board:list):
    pass
# 10. Number of attacking pawns (i.e. positioned in three topmost rows);
def attacking_pieces(board:list):
    pass
# 11. Number of centrally positioned pawns (i.e. situated on the eight central squares of the board);
def central_pawns(board:list):
    pass
# 12. Number of centrally positioned kings;
def central_queens(board:list):
    pass
# 13. Number of pawns positioned on the main diagonal;
def main_diagonal_pawns(board:list):
    # x == (BOARD_HEIGHT-y)
    pass
# 14. Number of kings positioned on the main diagonal;
def main_diagonal_queens(board:list):
    pass
# 15. Number of pawns situated on double diagonal;
def double_diagonal_pawns(board:list):
    pass
# 16. Number of kings situated on double diagonal;
def double_diagonal_queens(board:list):
    pass
# 17. Number of loner pawns. Loner piece is defined as the one not adjacent to any other
def loner_pawns(board:list):
    pass
# 18. Number of loner kings;
def loner_kings(board:list):
    pass
# 19. Number of holes, i.e. empty squares adjacent to at least three pieces of the same color.
    # Apart from the above parameters six patterns were defined. They are described below
    # using common notation presented in Fig. 2. Since only one instance of each pattern can
    # exist for any of the players at the same time, features 20− 25 can take only boolean values.
# 20. Presence of a Triangle pattern(see Fig. 3(a)).
# 21. Presence of an Oreo pattern (see Fig. 3(b)).
# 22. Presence of a Bridge pattern (see Fig. 3(c)).
# 23. Presence of a Dog pattern (see Fig. 3(d)).
# 24. Presence of a pawn in corner (i.e. White (Black) pawn on square 29 (4), resp.);
# 25. Presence of a king in corner (i.e. White (Black) king on square 4 (29), resp.);
# https://pages.mini.pw.edu.pl/~mandziukj/PRACE/es_init.pdf

# def evaluate(board,param_list:list[]):
#     return p1*param_list[0] + ... + 