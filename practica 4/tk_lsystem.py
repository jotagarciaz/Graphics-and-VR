#https://github.com/ambron60/l-system-drawing/edit/master/lsystem.py
import turtle
import tkinter as tk
from tkinter import ttk
import copy
import math

SYSTEM_RULES = {}  

class Aplicacion(tk.Tk):
	def __init__(self):
		self.ventana1=tk.Tk()
		self.height = 512
		self.width = 640
		self.margin = 20
		self.ventana1.geometry('1000x800')
		self.entradadatos()
		self.canvas1=tk.Canvas(self.ventana1, width=self.width+2*self.margin, height=self.height+2*self.margin, background="white")
		self.canvas1.grid(column=0, row=1)
		self.points = [] #type: list
		self.draw()
		self.ventana1.mainloop()

	def origin(self, y_coordinate):
		y_coordinate = self.canvas1.winfo_height() - y_coordinate
		return y_coordinate

	def entradadatos(self):
		self.lf1=ttk.LabelFrame(self.ventana1, text="Choose your data.")
		self.lf1.grid(column=0, row=0)
		
        self.label1=ttk.Label(self.lf1, text="Enter rule: (0 when done):")
		self.label1.grid(column=0,row=0, padx=5, pady=5)
		self.dato=tk.StringVar()
		
        self.label2 = ttk.Label(self.lf1, text="Enter axiom (w):")
		self.label2.grid(column=0,row=1, padx=5, pady=5)
		self.level=tk.StringVar()
        
        self.label2 = ttk.Label(self.lf1, text="Enter number of iterations (n):")
		self.label2.grid(column=0,row=1, padx=5, pady=5)
		self.level=tk.IntVar()

        self.label2 = ttk.Label(self.lf1, text="Enter step size (segment length): ")
		self.label2.grid(column=0,row=1, padx=5, pady=5)
		self.level=tk.IntVar()

        self.label2 = ttk.Label(self.lf1, text="Enter initial heading (alpha-0):  ")
		self.label2.grid(column=0,row=1, padx=5, pady=5)
		self.level=tk.IntVar()

        self.label2 = ttk.Label(self.lf1, text="Enter angle increment (i): ")
		self.label2.grid(column=0,row=1, padx=5, pady=5)
		self.level=tk.IntVar()

		self.level=ttk.Entry(self.lf1, textvariable=self.level, width=3, justify=tk.CENTER)
		self.level.grid(column=1, row=2, padx=5, pady=5)
		self.level.insert(tk.INSERT, "1")
		self.boton1=ttk.Button(self.lf1, text="Transform", command=self.draw)
		self.boton1.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky="we")

    def draw(self):
		self.canvas1.delete("all")
		if self.dato.get() == 1:
			level = int(self.level.get())
			x1 = self.margin + 0 
			y1 = self.margin + self.height
			x2 = self.margin + self.width/2
			y2 = self.margin + 0
			x3 = self.margin + self.width
			y3 = self.margin + self.height
			self.sierp_triangle(level, x1, y1, x2, y2, x3, y3)
		elif self.dato.get() == 2:
			level = int(self.level.get())
			x1 = self.margin 
			y1 = self.margin
			x2 = self.width - self.margin 
			y2 = self.height - self.margin  
			self.sierp_carpet(level, x1, y1, x2, y2)
		elif self.dato.get() == 3:
			level = int(self.level.get())
			x1 = self.margin + 0 
			y1 = self.margin + self.height
			x4 = self.margin + self.width/2
			y4 = self.margin + 0
			self.koch_curve(level, x1, y1, x4, y4)

def derivation(axiom, steps):
    derived = [axiom]  
    for _ in range(steps):
        next_seq = derived[-1]
        next_axiom = [rule(char) for char in next_seq]
        derived.append(''.join(next_axiom))
    return derived


def rule(sequence):
    if sequence in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequence


def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle):
    stack = []
    for command in SYSTEM_RULES:
        turtle.pd()
        if command in ["F", "G", "R", "L"]:
            turtle.forward(seg_length)
        elif command == "f":
            turtle.pu()  
            turtle.forward(seg_length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()  
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)


def set_turtle(alpha_zero):
    r_turtle = turtle.Turtle()  
    r_turtle.screen.title("L-System Derivation")
    r_turtle.speed(0)  # (0 = más rápido)
    r_turtle.setheading(alpha_zero)  
    return r_turtle


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

    model = derivation(axiom, iterations)  

    segment_length = int(input("Enter step size (segment length): "))
    alpha_zero = float(input("Enter initial heading (alpha-0): "))
    angle = float(input("Enter angle increment (i): "))

   
    r_turtle = set_turtle(alpha_zero)  
    turtle_screen = turtle.Screen()  
    turtle_screen.screensize(1500, 1500)
    draw_l_system(r_turtle, model[-1], segment_length, angle)  
    turtle_screen.exitonclick()


if __name__ == "__main__":
    main()
