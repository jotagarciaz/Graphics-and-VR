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

        x1 = self.margin 
        y1 = self.margin
        x2 = self.width - self.margin 
        y2 = self.height - self.margin  

    
        
        self.recursion(level, x1, y1, x2, y2)

    def recursion(self, level, x1, y1, x2, y2):

        if level < 1:
            self.canvas.create_rectangle(x1,y1,x2,y2)

        else:
            level -=1
            x_0 = x1
            y_0 = y1
            
            x_02 = x2
            y_02 = y2
            
            x_1 = (x2/3) + ((x1/3)*2)
            y_1 = (y1/3) + ((y2/3)*2)

            x_2 = ((x2/3)*2) + (x1/3)
            y_2 = ((y1/3)*2) + (y2/3)




            self.recursion(level , x_0,y_0,x_1,y_2)
            self.recursion(level , x_1, y_0,x_2, y_2)
            self.recursion(level , x_2, y_0,x_02, y_2)
            self.recursion(level , x_0, y_2,x_1, y_1)
            self.recursion(level , x_2, y_2,x_02, y_1)
            self.recursion(level , x_0, y_1,x_1, y_02)
            self.recursion(level , x_1, y_1,x_2, y_02)
            self.recursion(level , x_2, y_1,x_02,y_02)

# create and start main window
MainWindow()