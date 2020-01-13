import math
import tkinter as tk

angles = [math.radians(60*x) for x in range(6)]
sines = [math.sin(x) for x in angles]
cosin = [math.cos(x) for x in angles]

def L(angle, coords, jump):
    return (angle + 1) % 6
def R(angle, coords, jump):
    return (angle + 4) % 6
def F(angle, coords, jump):
    coords.append(
        (coords[-1][0] + jump * cosin[angle],
         coords[-1][1] + jump * sines[angle]))
    return angle

decode = dict(L=L, R=R, F=F)

def koch(steps, length=200, startPos=(0,0)):
    pathcodes="F"
    for i in range(steps):
        pathcodes = pathcodes.replace("F", "FLFRFLF")

    jump = float(length) / (3 ** steps)
    coords = [startPos]
    angle = 0

    for move in pathcodes:
        angle = decode[move](angle, coords, jump)

    return coords


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
        level = int(self.level.get())

        points = koch(level,TOTALWIDTH,(-TOTALWIDTH/2,0))

        for i in range(0,len(points)-1):
            self.canvas.create_line(points[i], points[i+1])


TOTALWIDTH = 1000
MainWindow()