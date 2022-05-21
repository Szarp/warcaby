
class Pawn:
	def __init__(self, color:str, position):
		self.color:str = color
		self.position = position
		self.is_queen:bool = False
		self.is_captured:bool = False
		self.black_pawn = 'b'
		self.black_king = 'B'
		self.white_pawn = 'w'
		self.white_king = 'W'

	def print(self):
		print('Color: ' , self.color)
		print(f'Position: {self.position} ')
		print('Queen: ' , self.is_queen)
        # print("is_captured",is)

	def color_letter(self):
		if self.is_queen:
			return self.white_king if self.color == 'white' else self.black_king
		return self.white_pawn if self.color == 'white' else self.black_pawn
		