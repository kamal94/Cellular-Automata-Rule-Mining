import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, size):
        tk.Tk.__init__(self)
        self.size = size
        self.canvas = tk.Canvas(self, width=size*10, height=size*10, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = size
        self.columns = size
        self.cellwidth = 10
        self.cellheight = 10

        self.rect = {}
        self.oval = {}
        for column in range(size):
            for row in range(size):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")
                self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="black", tags="oval")

        self.redraw(1000)

    def redraw(self, delay):
        # self.canvas.itemconfig("rect", fill="blue")
        # self.canvas.itemconfig("oval", fill="blue")
        # for i in range(10):
        #     row = random.randint(0,19)
        #     col = random.randint(0,19)
        #     item_id = self.oval[row,col]
        #     self.canvas.itemconfig(item_id, fill="green")
        self.after(delay, lambda: self.redraw(delay))

    def draw_result(self, data):
        for row in range(self.size):
            for col in range(self.size):
                item_id = self.oval[row,col]
                if data[row][col] == 1:
                    self.canvas.itemconfig(item_id, fill="red")
                else:
                    self.canvas.itemconfig(item_id, fill="black")


if __name__ == "__main__":
    app = App(30)
    app.mainloop()