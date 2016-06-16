class OneD:
	from loc import loc as Loc

	def rule_30(neighbors):
		p1,p2,p3 = neighbors
		if (p1) != (p2 or p3):
			return 1
		else:
			return 0


	def __init__(self, size=20, r=3, k=2, rule=rule_30, RIC=False):
		"""Initializes the simulation with the passed parameters.
		parameters: 
			size: The size of the simulation. The simulation will be square according to this parameter. Defaults to 20
			r: The number of neighbors that will be evaluated by the rule function. Defaults to 3
			k: The number of possible states in the system. The minimum value is 2. The states are represented as numbers
			beginning with 0. Defaults to 2
			rule: A function that accepts a tuple of r variables representing the neighbors and returns one of
				k states. Defaults to rule 30
			RIC (Rancom Initial Condition): a boolean variable that specifies if the simulation should start from a random
				initial state. If True is passed, each cell in the first row will be initialized to one of the k states.
				 Defaults to Fales. 
		"""
		from lattice import lattice
		from loc import loc as Loc
		import random

		self.size = size
		self.r = r
		self.k = k
		self.rule = rule
		self.__ran = False
		self.state = lattice(self.size)
		if RIC:
			for i in range(size):
				if random.random() <= 1/k:
					self.state.set_cell(Loc(0, i), 1)
		else:
			self.state.set_cell(Loc(0, int(size/2)), 1)

	def default_neighbors(self, loc: Loc):
		"""Returns the locations of the three cells atop this cell"""
		return (self.state.offset(loc, -1,-1), self.state.offset(loc, -1), self.state.offset(loc, -1, 1))


	def neighbor_locs(self, loc:Loc, neighbors=default_neighbors):
		"""Returns the location of the neighbors of the cell at the specified location.
		If no function is pased to determine the location of the neighbors, then the 
		3 neighbors atop the cell are chosen by default.
		parameters:
			loc: The location of the cell
			neighbors: A function that maps the neighbors from the given loc.
		"""
		return neighbors(self,loc)


	def neighbor_vals(self, loc:Loc):
		""" Returns the value of the neighbord depending on the neighbor_locs 
		parameters:
			loc: The location of which to get the values of the neighbors
		"""
		return [self.state.lat()[l.row()][l.col()] for l in self.neighbor_locs(loc)]


	def run(self):
		"""Runs the cellular automata simulation based on the passed rule."""
		from loc import loc as Loc
		for r in range(1,self.size):
			for c in range(self.size): 
				this = Loc(r,c)
				self.state.set_cell(this, self.rule(self.neighbor_vals(this)))
		self.__ran = True

	def extract_data(self):
		"""Returns a list of tuples, each of which contains r+1 entries,
		where r is the number of neighbors. The first r numbers in the tuples
		represent the state of the neighbors, and the (r+1)st entry represents
		the state of the resulting cell."""
		from loc import loc as Loc
		data = []
		if self.__ran == False:
			self.run()
		for row in range(1, self.size):
			for col in range(0, self.size):
				this = Loc(row,col)
				data.append( tuple( self.neighbor_vals(this)) + tuple([self.state.lat()[row][col]]) )
		return data



	def __iter__(self):
		return self.state.__iter__()

	def __repr__(self):
		return str(self.state)