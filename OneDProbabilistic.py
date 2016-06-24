from OneD import OneD
class OneDProbabilistic(OneD):


	def default_rule(neighbors, prob=0.9):
		"""implements the rule_30 CA rule but gives the rule a 
		propagation probability of 90%
		"""
		from random import random
		p1,p2,p3 = neighbors
		if (p1) != (p2 or p3):
			if random() < prob:
				return 1
			else:
				return 0
		else:
			if random() < prob:
				return 0
			else:
				return 1

	def run(self):
		"""Runs the cellular automata simulation based on the passed rule."""
		from loc import loc as Loc
		for r in range(1,self.size):
			for c in range(self.size): 
				this = Loc(r,c)
				self.state.set_cell(this, self.rule(self.neighbor_vals(this), self.__prob))
		self.__ran = True

	def __init__(self, size=20, r=3, k=2, rule=default_rule, RIC=False):
		self.__prob = 0.9
		super(OneDProbabilistic, self).__init__(size, r, k, rule, RIC)

	def set_prob(self, prob:float):
		self.__prob = prob