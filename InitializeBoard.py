from tkinter import N
from tkinter.messagebox import NO
from Pawn import Pawn

BOARD_WIDTH:int = 8
BOARD_HEIGHT:int = 8

def initialize_board():
	list:list = []
	for x in range(BOARD_WIDTH):
		for y in range(BOARD_HEIGHT):
			if ((x + y) % 2 == 0):
				if (y < 3):
					pawn:Pawn = Pawn('white', [y,x])
					list.append(pawn)
				if (y > 4):
					pawn:Pawn = Pawn('black', [y,x])
					list.append(pawn)

	return list
# LUUKIER SYNKTAKTYCZNY ;)
def print_board(pawns)-> None:
	white_square_code = f'\u25A1'
	# x  = '\u26c0 \u26c1 \u26c2 \u26c3'
	print('  0 1 2 3 4 5 6 7 ')
	for x in range(BOARD_WIDTH):
		row:str = str(BOARD_WIDTH - x - 1) + ' '
		for y in range(BOARD_HEIGHT):
			pawn = get_pawn(pawns, [x,y])
			if pawn:
				row += pawn.color_letter() + ' '
			else:
				row += ' ' if (x + y) % 2 == 0 else white_square_code
				row += ' '
		row += str(BOARD_WIDTH - x - 1)
		print(row)
	print('  0 1 2 3 4 5 6 7 ')

def get_pawn(pawns, position) -> Pawn:
	pawn = list(filter(lambda pawn: pawn.position == position, pawns))
	return None if not pawn else pawn[0]

def move_pawn(pawn, position) -> None:
	pawn.position = position

def get_pawn_moves(pawns, pawn):
	# jak moge otrzyamc liste czarnych i białych klockow?
	captures =  get_captures(pawns, pawn)
	if (captures):
		return captures
	return get_forward_moves(pawns, pawn)

def get_captures(pawns, pawn):
	positions = []
	fields = []
	positions.append([-1, -1])
	positions.append([-1, 1])
	positions.append([1, -1])
	positions.append([1, 1])
	for position in positions:
		calculated_position = sum_positions(zip(position, pawn.position))
		if (not in_between_board(calculated_position)):
			continue
		other_pawn = get_pawn(pawns, calculated_position)
		if (other_pawn):
			if (other_pawn.color != pawn.color):
				calculated_position = sum_positions(zip(calculated_position, position))
				if (in_between_board(calculated_position) and get_pawn(pawns, calculated_position)):
					fields.append(calculated_position)

	return fields

# def get_position_after_capture:

def get_color_pawns(color, pawns):
	return list(filter(lambda pawn: pawn.color == color, pawns))
	
def get_forward_moves(pawn, pawns):
	positions = []
	fields = []
	if (pawn.color == 'black'):
		positions.append([-1, -1])
		positions.append([1, -1])
	else:
		positions.append([1, 1])
		positions.append([-1, 1])
	for position in positions:
		calculated_position = sum_positions(zip(position, pawn.position))
		if (not in_between_board(calculated_position)):
			continue
		if (get_pawn(pawns, calculated_position)):
			continue
		fields.append(calculated_position)

	return fields

def sum_positions(zipped_positions):
	return [x + y for(x,y) in zipped_positions]

def in_between_board(position):
	return (position[0] >= 0 and position[0] <= 7 and position[1] >= 0 and position[1] <= 7)