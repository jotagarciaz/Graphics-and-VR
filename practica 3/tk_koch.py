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
        x4 = self.margin + self.width/2
        y4 = self.margin + 0
        
        self.recursion(level, x1, y1, x4,y4)

    def recursion(self, level, x1, y1,x4,y4):

        if level <= 1:
            
            self.canvas.create_line(x1, y1, x4, y4)

        else:
            level = level - 1
            Dx = (x4 - x1) / 3
            Dy = (y4 - y1) / 3
            x2 = x1 + Dx
            y2 = y1 + Dy
            x3 = x2 + Dx
            y3 = y2 + Dy
            x = (Dx - math.sqrt(3) * Dy)/2 + (x1 + Dx)
            y = (math.sqrt(3) * Dx + Dy)/2 + (y1 + Dy)

            self.recursion(level,x1, y1, x2, y2)
            self.recursion(level, x2, y2, x, y)
            self.recursion(level,x, y, x3, y3 )
            self.recursion(level,x3, y3, x4, y4 )

# create and start main window
MainWindow()