class loc:
	def __init__(self, row:int, col:int):
		"""initializes the location object with a row and column.
			Parameters:
				row: the row of the location
				col: the column of the location
		"""
		self.__row = row
		self.__col = col

	def row(self):
		"""Returns the row of the location"""
		return self.__row

	def col(self):
		"""Returns the column of the location"""
		return self.__col

	def __repr__(self):
		return "(" + str(self.row()) + "," + str(self.col()) + ")"