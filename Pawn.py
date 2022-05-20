
class Pawn:
	def __init__(self, color:str, position):
		self.color:str = color
		self.position = position
		self.is_queen:bool = False
		self.is_removed:bool = False
		self.black_pawn = 'b'
		self.black_king = 'B'
		self.white_pawn = 'w'
		self.white_king = 'W'

	def print(self):
		print('Color: ' , self.color)
		print(f'Position: {self.position} ')
		print('Queen: ' , self.is_queen)

	def color_letter(self):
		return self.white_pawn if self.color == 'white' else self.black_pawn
		