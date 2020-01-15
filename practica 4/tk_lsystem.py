import tkinter as tk
import math

SYSTEM_RULES = {}  # generator system rules for l-system


def derivation(axiom, steps):
    derived = [axiom]  # seed
    for _ in range(steps):
        next_seq = derived[-1]
        next_axiom = [rule(char) for char in next_seq]
        derived.append(''.join(next_axiom))
    return derived


def rule(sequence):
    if sequence in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequence



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

    #habría que traducir draw para que imite las funciones de draw_l_system
    def draw(self):
        # clear canvas
        self.canvas.delete("all")

        level = int(self.level.get())

        stack = []
        for command in SYSTEM_RULES:
             if command in ["F", "G", "R", "L"]:
                 self.canvas.create_line(self.margin,self.margin,seg)
        
        self.recursion(level, x1, y1, x2, y2)

def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle):
    stack = []
    for command in SYSTEM_RULES:
        turtle.pd()
        if command in ["F", "G", "R", "L"]:
            turtle.forward(seg_length)
        elif command == "f":
            turtle.pu()  # pen up - not drawing
            turtle.forward(seg_length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()  # pen up - not drawing
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)




def main():
    rule_num = 1
    while True:
        rule = input("Enter rule[%d]:rewrite term (0 when done): " % rule_num)
        if rule == '0':
            break
        key, value = rule.split("->")
        SYSTEM_RULES[key] = value
        rule_num += 1

    axiom = input("Enter axiom (w): ")
    iterations = int(input("Enter number of iterations (n): "))

    model = derivation(axiom, iterations)  # axiom (initial string), nth iterations

    segment_length = int(input("Enter step size (segment length): "))
    alpha_zero = float(input("Enter initial heading (alpha-0): "))
    angle = float(input("Enter angle increment (i): "))

    
    draw_l_system(r_turtle, model[-1], segment_length, angle)  # draw model
    


MainWindow()