from ast import Return
from tkinter import N
from tkinter.messagebox import NO

# from matplotlib.pyplot import get
from Pawn import Pawn
import copy

BOARD_WIDTH: int = 8
BOARD_HEIGHT: int = 8
WHITES_WIN_MESSAGE: str = "Whites win"
BLACKS_WIN_MESSAGE: str = "Blacks win"
DRAW_MESSAGE: str = "Draw"


def initialize_board(rows_of_pawns: int = 3):
    pawns: list = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if (x + y) % 2 == 1:
                if y < rows_of_pawns:
                    pawn: Pawn = Pawn("black", [y, x])
                    pawns.append(pawn)
                if y > BOARD_HEIGHT - rows_of_pawns - 1:
                    pawn: Pawn = Pawn("white", [y, x])
                    pawns.append(pawn)
    return pawns


def simulation(pawns):
    board: list = []
    for x in pawns:
        pawn: Pawn = Pawn(x.color, x.position)
        board.append(pawn)
    return board


def can_color_capture(color, pawns):
    color_pawns = get_color_pawns(color, pawns)
    for pawn in color_pawns:
        _, capture = get_available_captures(pawns, pawn)
        if capture:
            return True
    return False


def get_all_possible_moves(color, pawns):
    all_moves = []
    color_pawns = get_color_pawns(color, pawns)
    can_capture = can_color_capture(color, pawns)
    max_captures = 0
    for pawn in color_pawns:
        is_capture, max, moves = get_pawn_moves(pawns, pawn)
        if can_capture:
            if not is_capture:
                continue
            if max > max_captures:
                all_moves = []
                max_captures = max
            if max == max_captures:
                for move in moves:
                    all_moves.append([pawn, move])
        else:
            for move in moves:
                all_moves.append([pawn, [move]])
    return (can_capture, all_moves)


def get_pawn_between(pawns, first_position, second_position):
    distance = sub_positions(zip(second_position, first_position))
    x_sign = 1 if distance[0] > 0 else -1
    y_sign = 1 if distance[1] > 0 else -1
    vector = [x_sign, y_sign]
    calculated_position = first_position
    calculated_position = sum_positions(zip(calculated_position, vector))
    while is_on_board(calculated_position):
        i, pawn = get_pawn(pawns, calculated_position)
        if pawn:
            return i
        calculated_position = sum_positions(zip(calculated_position, vector))
    return


def build_board_from_move(board, move_is_capture, moves):
    board = [copy.deepcopy(pawn) for pawn in board]
    pawn, move_path = moves
    pawn_position = pawn.position
    _, pawn = get_pawn(board, pawn_position)
    if move_is_capture:
        for move in move_path:
            perform_capture(board, pawn, move)
    else:
        perform_move(pawn, move_path[0])
    promotion(pawn)
    return board


def promotion(pawn):
    if pawn.color == "white" and pawn.position[0] == 0:
        pawn.is_queen = True
    if pawn.color == "black" and pawn.position[0] == BOARD_HEIGHT - 1:
        pawn.is_queen = True


def perform_capture(board, pawn, position):
    del board[get_pawn_between(board, pawn.position, position)]
    move_pawn(pawn, position)


def perform_move(pawn, position):
    move_pawn(pawn, position)


def game_status(pawns, color, queen_moves=0):
    blacks = get_color_pawns("black", pawns)
    whites = get_color_pawns("white", pawns)
    can_white_move = False
    can_black_move = False
    if not blacks:
        return WHITES_WIN_MESSAGE
    if not whites:
        return BLACKS_WIN_MESSAGE

    for pawn in blacks:
        _, _, moves = get_pawn_moves(pawns, pawn)
        if moves:
            can_black_move = True
            break

    for pawn in whites:
        _, _, moves = get_pawn_moves(pawns, pawn)
        if moves:
            can_white_move = True
            break

    if not can_black_move and not can_white_move:
        return DRAW_MESSAGE

    if color == "white":
        if not can_white_move:
            return BLACKS_WIN_MESSAGE

    if color == "black":
        if not can_black_move:
            return WHITES_WIN_MESSAGE
    if queen_moves > 15:
        return DRAW_MESSAGE

    return


def print_board(pawns) -> None:
    white_square_code = "▒▒▒║"
    title = "  │"
    row_split = "══" + "╬═══" * (BOARD_WIDTH + 1)
    for k in range(BOARD_WIDTH):
        title += f" {k} ║"
    print(title)
    print(row_split)
    for x in range(BOARD_WIDTH):
        row: str = str(x) + " │"
        for y in range(BOARD_HEIGHT):
            _, pawn = get_pawn(pawns, [x, y])
            if pawn:
                row += f" {pawn.color_letter()} ║"
            else:
                row += "   ║" if (x + y) % 2 == 1 else white_square_code
                row += ""
        row += str(x)
        print(row)
        print(row_split)
    print(title)


def get_pawn(pawns, position) -> Pawn:
    for i, pawn in enumerate(pawns):
        if pawn.position == position:
            return (i, pawn)
    return (-1, None)


def is_free(pawns, position):
    for pawn in pawns:
        if pawn.position == position:
            return False
    return True


def move_pawn(pawn, position) -> None:
    pawn.position = position


def get_most_captures(pawns, pawn):
    temp_pawn = copy.deepcopy(pawn)
    pawns.remove(pawn)
    captures = get_captures(pawns, temp_pawn)
    pawns.append(temp_pawn)
    if not captures:
        return 0, None
    captures = flatten(captures)
    max = 0
    longest_captures = []
    for capture in captures:
        if len(capture) > max:
            max = len(capture)
            longest_captures = []
        if len(capture) == max:
            longest_captures.append(capture)
    return max, longest_captures


def flatten(moves):
    all_moves = []
    if type(moves[0][0]) is not list:
        return [moves]
    for move in moves:
        all_moves.extend(flatten(move))
    return all_moves


def get_pawn_moves(pawns, pawn):
    max, captures = get_most_captures(pawns, pawn)
    if captures:
        return True, max, captures
    return False, 0, get_forward_moves(pawns, pawn)


def available_capture_positions(pawn):
    positions = []
    vectors = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
    for position in vectors:
        calculated_position = sum_positions(zip(position, pawn.position))
        if is_on_board(calculated_position):
            positions.append(position)
    return positions


def get_available_captures(pawns, pawn):
    available_capture_moves = []
    captured_enemies_index = []
    if len(pawns) == len(get_color_pawns(pawn.color, pawns)):
        return (captured_enemies_index, available_capture_moves)
    positions = available_capture_positions(pawn)
    for pos in positions:
        if pawn.is_queen:
            enemy_position = pawn.position
            while True:
                enemy_position = sum_positions(zip(pos, enemy_position))
                if not is_on_board(enemy_position):
                    break
                i, other_pawn = get_pawn(pawns, enemy_position)
                if other_pawn != None:
                    if other_pawn.is_captured == True:
                        break
                    if other_pawn.color != pawn.color:
                        position_after_capture = enemy_position
                        while True:
                            position_after_capture = sum_positions(zip(position_after_capture, pos))
                            if is_on_board(position_after_capture):
                                if is_free(pawns, position_after_capture):
                                    available_capture_moves.append(position_after_capture)
                                    captured_enemies_index.append(i)
                                else:
                                    break
                            else:
                                break
        else:
            enemy_position = sum_positions(zip(pos, pawn.position))
            i, other_pawn = get_pawn(pawns, enemy_position)
            if other_pawn != None:
                if other_pawn.is_captured == True:
                    continue
                if other_pawn.color != pawn.color:
                    position_after_capture = sum_positions(zip(enemy_position, pos))
                    if is_on_board(position_after_capture) and is_free(
                        pawns, position_after_capture
                    ):
                        available_capture_moves.append(position_after_capture)
                        captured_enemies_index.append(i)

    return (captured_enemies_index, available_capture_moves)


def get_captures(pawns, pawn, previous_capture: list = []):
    pawn = copy.deepcopy(pawn)
    captured_enemies_index, available_capture_moves = get_available_captures(pawns, pawn)
    next_captures = []
    fields = []
    if len(available_capture_moves) > 0:
        for k in range(len(available_capture_moves)):
            uncaptured_pawns = pawns.copy()
            uncaptured_pawns[captured_enemies_index[k]].is_captured = True
            move_pawn(pawn, available_capture_moves[k])  # [[0,0]]
            prev = previous_capture.copy()
            prev.append(available_capture_moves[k])
            next_captures = get_captures(uncaptured_pawns, pawn, prev.copy())
            uncaptured_pawns[captured_enemies_index[k]].is_captured = False
            if len(next_captures) > 0:
                fields.append(next_captures.copy())
        return fields
    return previous_capture


def get_color_pawns(color, pawns):
    return list(filter(lambda pawn: pawn.color == color, pawns))


def get_forward_moves(pawns, pawn):
    fields = []
    if pawn.is_queen:
        positions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    elif pawn.color == "black":
        positions = [[1, 1], [1, -1]]
    else:
        positions = [[-1, 1], [-1, -1]]
    for position in positions:
        calculated_position = pawn.position
        calculated_position = sum_positions(zip(position, calculated_position))
        if pawn.is_queen:
            while True:
                if not is_on_board(calculated_position):
                    break
                _, other_pawn = get_pawn(pawns, calculated_position)
                if other_pawn:
                    break
                fields.append(calculated_position)
                calculated_position = sum_positions(zip(position, calculated_position))
        else:
            if not is_on_board(calculated_position):
                continue
            _, other_pawn = get_pawn(pawns, calculated_position)
            if other_pawn:
                continue
            fields.append(calculated_position)

    return fields


def get_queen_moves(pawn, pawns):
    positions = []
    positions.append([-1, -1])
    positions.append([-1, 1])
    positions.append([1, -1])
    positions.append([1, 1])
    captures = get_queen_captures(pawn, pawns, positions)
    if captures:
        return captures
    fields = []
    for position in positions:
        calculated_position = sum_positions(zip(position, pawn.position))
        while True:
            calculated_position = sum_positions(zip(position, pawn.position))
            if not is_on_board:
                break
            other_pawn = get_pawn(pawns, calculated_position)
            if not other_pawn:
                fields.append(calculated_position)
            else:
                break
    return fields


def get_queen_captures(pawn, pawns, positions):
    fields = []
    for position in positions:
        calculated_position = sum_positions(zip(position, pawn.position))
        while True:
            calculated_position = sum_positions(zip(position, pawn.position))
            if not is_on_board:
                break
            other_pawn = get_pawn(pawns, calculated_position)
            if other_pawn:
                if other_pawn.color != pawn.color:
                    calculated_position = sum_positions(zip(position, pawn.position))
                    if is_on_board(calculated_position) and not get_pawn(
                        pawns, calculated_position
                    ):
                        fields.append(sub_positions(zip(pawn.position, calculated_position)))
                        break

    return fields


def sum_positions(zipped_positions):
    return [x + y for (x, y) in zipped_positions]


def sub_positions(zipped_positions):
    return [x - y for (x, y) in zipped_positions]


def is_on_board(position) -> bool:
    return (
        position[0] >= 0
        and position[0] <= BOARD_WIDTH - 1
        and position[1] >= 0
        and position[1] <= BOARD_WIDTH - 1
    )
