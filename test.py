import OneD
import OneDProbabilistic
from loc import loc as Loc
from gui import App
import numpy as np

o = OneDProbabilistic.OneDProbabilistic(100, RIC=True)


o.set_prob(1)
o.run()
# Function will print board like an actual board
# def print_board(board):
#   for row in board:
#     print ("".join(row))
data = o.extract_data()

file = open("one_dimension_prob"+str("test")+".csv", "w")
file.write("p1, p2, p3, s \n")
for p1,p2,p3,s in data:
	file.write(str(p1) + "," + str(p2) + "," + str(p3) + "," + str(s) + "\n")