import OneD
from loc import loc as Loc
from yest import App

o = OneD.OneD(100, RIC=True)

o.run()
# Function will print board like an actual board
def print_board(board):
  for row in board:
    print ("".join(row))

data = o.extract_data()

file = open("one_dimension.csv", "w")
file.write("p1, p2, p3, s \n")
for p1,p2,p3,s in data:
	file.write(str(p1) + "," + str(p2) + "," + str(p3) + "," + str(s) + "\n")

# a = App(o.size)
# a.draw_result(o.state.lattice)
# a.mainloop()
