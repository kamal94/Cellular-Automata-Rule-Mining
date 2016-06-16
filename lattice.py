class lattice:
	import loc as Loc

	def __init__(self, size = 5, k=2, dimension=2):
		"""initialized the lattice object.
		parameter:
			size: the size of the lattice 
			k: the number of possible states. Defaluts to 2. THIS IS NOT IMPLEMENTED
			dimension: the dimension of the lattice. Defaults to 2. THIS IS NOT IMPLEMENTED
		"""
		self.__iter_ind = 0
		self.__k = k
		self.__dimension = dimension
		self.lattice = [[0]*size for _ in range(size)]
		self.size = size

	def set_cell(self, loc:Loc , new_state:int):
		self.lattice[loc.row()][loc.col()] = new_state

	def lat(self):
		return self.lattice

	def offset(self, location:Loc, row=0, col=0):
		"""returns a location with the specified row and column offsets.
		parameters:
			location: The location object used as a base.
			col: The column offset by which to move location. Can be negative or positive.
			row: The row offset by which to move location. Can be negative or positive.
		"""
		import loc as Loc
		t_col = (location.col()+col) % self.size
		t_row = (location.row()+row) % self.size	
		return Loc.loc(t_row, t_col)

	def __iter__(self):
		return self

	def __next__(self):
		"""Iterates through the rows in the lattice"""
		if self.__iter_ind >= self.size:
			self.__iter_ind = 0
			raise StopIteration
		row = self.lattice[self.__iter_ind]
		self.__iter_ind += 1
		return row

	
	def __repr__(self):
		"""Returns the lattice in a string format"""
		return str(self.lat())
