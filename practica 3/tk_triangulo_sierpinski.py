#editar, original en https://stackoverflow.com/questions/33970499/python-tkinter-coding-a-sierpinski-triangle-in-an-objective-orientated-method

import tkinter as tk
import math

class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Fractal")

        self.width = 512
        self.height = int(round(self.width*math.sqrt(3.0)/2.0))
        self.margin = 10

        self.canvas = tk.Canvas(self, width=self.width+(2*self.margin), height=self.height+(2*self.margin), bg="white")
        self.canvas.pack()

        self.btn = tk.Button(self, text="Draw", command=self.draw)
        self.btn.pack(side=tk.LEFT)

        self.label = tk.Label(self, text="Level")
        self.label.pack()

        self.level = tk.Entry(self, width=3, justify=tk.CENTER)
        self.level.insert(tk.INSERT, "1")
        self.level.pack()

        self.mainloop()        

    def draw(self):
        # clear canvas
        self.canvas.delete("all")

        level = int(self.level.get())

        x1 = self.margin + 0 
        y1 = self.margin + self.height
        x2 = self.margin + self.width/2
        y2 = self.margin + 0
        x3 = self.margin + self.width
        y3 = self.margin + self.height

        self.recursion(level, x1, y1, x2, y2, x3, y3)

    def recursion(self, level, x1, y1, x2, y2, x3, y3):
        print("level:", level)

        if level <= 1:
            #print("   draw element")
            self.canvas.create_line(x1, y1, x2, y2,fill="red")
            self.canvas.create_line(x2, y2, x3, y3,fill="blue")
            self.canvas.create_line(x3, y3, x1, y1,fill="green")
        else:
            #print("   recursion")
            level = level - 1

            middle_x1 = (x1 + x2)/2
            middle_y1 = (y1 + y2)/2

            middle_x2 = (x2 + x3)/2
            middle_y2 = (y2 + y3)/2

            middle_x3 = (x3 + x1)/2
            middle_y3 = (y3 + y1)/2

            self.recursion(level, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3)
            self.recursion(level, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2)
            self.recursion(level, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3)

# create and start main window
MainWindow()